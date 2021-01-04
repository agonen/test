from datetime import timedelta
import json
from typing import Union

import redis

from site_checker.storage.base import AbstractStorage


class RedisStorage(AbstractStorage):
    def __init__(self, redis_config=None, expire_in_minutes=30, *args, **kwargs):
        """
        redis_config a dict containing redis config
        @param redis_config:
        @type redis_config:
        @param args:
        @type args:
        @param kwargs:
        @type kwargs:
        """
        redis_config = redis_config or dict(host='localhost', port=6379, db=0)
        self.redis = redis.Redis(**redis_config)
        self.expire_in_minutes = timedelta(minutes=expire_in_minutes)

    def _get(self, url, *args, **kwargs) -> Union[None, dict]:
        val = self.redis.get(url)
        if val is None:
            return None

        return json.loads(val)

    def _set(self, url, data: dict, *args, **kwargs):
        self.redis.setex(name=url, value=json.dumps(data), time=self.expire_in_minutes)
