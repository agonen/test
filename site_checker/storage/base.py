from abc import ABC, abstractmethod
from typing import Union


class AbstractStorage(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f'{self.__class__.__name__} must implement __init__()')

    def get(self, url, *args, **kwargs) -> Union[None, dict]:
        """
        Check if url is not Malicious for storage DB
        @param url:
        @type url:
        @return:
        @rtype:
        """
        return self._get(url, *args, **kwargs)

    @abstractmethod
    def _get(self, url, *args, **kwargs) -> Union[None, dict]:
        raise NotImplementedError(f'{self.__class__.__name__} must implement get')

    def set(self, url, data: dict, *args, **kwargs):
        """
        Save results in storage
        @param data:
        @type data:
        @param url:
        @type url:
        @return:
        @rtype:
        """
        return self._set(url, data, *args, **kwargs)

    @abstractmethod
    def _set(self, url, data: dict, *args, **kwargs) -> dict:
        raise NotImplementedError(f'{self.__class__.__name__} must implement get')
