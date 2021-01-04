from dataclasses import asdict
import os

from site_checker.storage.base import AbstractStorage
from site_checker.storage.redis_backend import RedisStorage
from site_checker.url_checker.base import AbstractUrlChecker
from site_checker.url_checker.virus_total import VirusTotalChecker

# TODO : should be factory method
storage: AbstractStorage = RedisStorage()
VIRUS_TOTAL_PUBLIC_API = 'VIRUS_TOTAL_PUBLIC_API'
api_key = os.getenv(VIRUS_TOTAL_PUBLIC_API)
assert api_key is not None, f'Environment variable {VIRUS_TOTAL_PUBLIC_API} is not set'
url_checker: AbstractUrlChecker = VirusTotalChecker(api_key=api_key)


def site_checker(url) -> dict:
    data = storage.get(url=url)
    if data:
        return data

    # TODO: @amihay use serializer instead of asdict

    data = asdict(url_checker.get(url))
    storage.set(url=url, data=data)
    return data
