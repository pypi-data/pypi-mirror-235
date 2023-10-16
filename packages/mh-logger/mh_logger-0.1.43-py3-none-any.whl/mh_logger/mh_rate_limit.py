from __future__ import annotations

import os
from abc import abstractmethod
from datetime import timedelta
from enum import Enum
from typing import Dict, Optional

from dateutil.relativedelta import relativedelta
from redis import Redis

ENABLE_RATE_LIMIT = os.getenv("ENABLE_RATE_LIMIT", "True") == "True"


class RateLimitException(Exception):
    rate_id: str

    def __init__(
        self,
        rate_id: str,
        rate_limit: Optional[float],
        rate_usage: Optional[int],
        hint: str = "",
    ):
        if hint:
            hint = " Hint :: " + hint
        super().__init__(
            f"Usage rate :: {rate_usage} exceeds rate_limit :: {rate_limit} with rate_id :: {rate_id}.{hint}"  # noqa
        )
        self.rate_id = rate_id


class Tier(Enum):
    FREE = "free"
    PRO = "pro"
    MANAGED = "managed"


UNLIMITED = float("inf")


class Counter:
    _redis_client: Redis

    def __init__(
        self,
        timedelta_: timedelta,
        redis_host: str,
        redis_port: int = 6379,
        redis_password: Optional[str] = None,
    ):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_password = redis_password
        self.timedelta_ = timedelta_

    @property
    def redis_client(self) -> Redis:
        if not hasattr(self, "_redis_client"):
            self._redis_client = Redis(
                host=self.redis_host,
                port=self.redis_port,
                password=self.redis_password,
            )
        return self._redis_client

    def incr(self, key: str) -> None:
        if self.redis_client.exists(key):
            self.redis_client.incr(key)
        else:
            self.redis_client.set(key, 1, ex=self.timedelta_)

    def get(self, key: str) -> int:
        return int(self.redis_client.get(key) or 0)


class ValidateRateLimitRedis:
    def __init__(
        self,
        rate_id: str,
        tier_limits: Dict[Tier, float],
        timedelta_: timedelta,
        redis_host: str,
        redis_port: int = 6379,
        redis_password: Optional[str] = None,
    ):
        assert (
            Tier.FREE in tier_limits and Tier.PRO in tier_limits
        ), f"ValidateRateLimit.tier_limits must declare rate limits for :: {Tier.FREE} and {Tier.PRO}"  # noqa

        self.rate_id = rate_id
        self.counter = Counter(
            timedelta_, redis_host, redis_port, redis_password
        )

        # Set special tier limits
        self.tier_limits = tier_limits
        self.tier_limits[Tier.MANAGED] = UNLIMITED

    def validate_user_rate(self, user_id: str) -> None:
        if not ENABLE_RATE_LIMIT:
            return

        key = f"{user_id}/{self.rate_id}"

        # Get user data
        user_tier = self.get_user_tier(user_id)
        user_rate = self.counter.get(key)

        # Check rate limit
        rate_limit = self.tier_limits.get(user_tier, -1)
        if user_rate >= rate_limit:
            raise RateLimitException(self.rate_id, rate_limit, user_rate)

        # Update user rate
        self.counter.incr(key)

    @abstractmethod
    def get_user_tier(self, user_id: str) -> Tier:
        ...


class ValidateRateLimitPostgres:
    def __init__(
        self,
        rate_id: str,
        tier_limits: Dict[Tier, float],
        window: relativedelta,
    ):
        assert (
            Tier.FREE in tier_limits and Tier.PRO in tier_limits
        ), f"ValidateRateLimit.tier_limits must declare rate limits for :: {Tier.FREE} and {Tier.PRO}"  # noqa

        self.rate_id = rate_id

        # Set special tier limits
        self.tier_limits = tier_limits
        self.tier_limits[Tier.MANAGED] = UNLIMITED
        self.window = window

    def validate_user_rate(self, *, session, user_id: str) -> ValidateRateLimitPostgres:
        if not ENABLE_RATE_LIMIT:
            return

        user_tier = self.get_user_tier(session=session, user_id=user_id)
        user_usage = self.get_user_rate_limit_usage(session=session, user_id=user_id)

        # Check rate limit
        rate_limit = self.tier_limits.get(user_tier, -1)
        if user_usage >= rate_limit:
            raise RateLimitException(self.rate_id, rate_limit, user_usage)

        return self

    @abstractmethod
    def get_user_tier(self, *, session, user_id: str) -> Tier:
        ...

    @abstractmethod
    def get_user_rate_limit_usage(self, *, session, user_id: str) -> int:
        ...

    @abstractmethod
    def increment_user_rate_usage(self, *, session, user_id: str, usage: int) -> int:
        ...