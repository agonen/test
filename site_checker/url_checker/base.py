from abc import ABC, abstractmethod

from site_checker.api.models import UrlResult


class AbstractUrlChecker(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f'{self.__class__.__name__} must implement __init__()')

    def get(self, url, *args, **kwargs) -> UrlResult:
        """
        Check if url is not Malicious
        @param url:
        @type url:
        @return:
        @rtype:
        """
        return self._get(url, *args, **kwargs)

    @abstractmethod
    def _get(self, url, *args, **kwargs) -> UrlResult:
        raise NotImplementedError(f'{self.__class__.__name__} must implement get')
