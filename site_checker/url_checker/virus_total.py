from pip._vendor.retrying import retry
from virus_total_apis import PublicApi as VirusTotalPublicApi

from site_checker.api.models import UrlResult, SiteRiskValues
from site_checker.url_checker.base import AbstractUrlChecker

BAD_SITES = ['phishing', 'malware', 'malicious']


class ApiLimitException(Exception):
    pass


def retry_if_api_limit(exception):
    return isinstance(exception, ApiLimitException)


class VirusTotalChecker(AbstractUrlChecker):
    def __init__(self, api_key, *args, **kwargs):
        self.vt = VirusTotalPublicApi(api_key=api_key)

    @staticmethod
    def _get_site_voting(scans: dict) -> dict:
        res = {}
        for _, v in scans.items():
            key = v['result'].split(' ')[0]
            res[key] = res.get(key, 0) + 1

        return res

    @staticmethod
    def _get_site_risks(site_voting: dict):
        if site_voting is None:
            return None
        return SiteRiskValues.risk if any(site_voting.get(x, 0) > 0 for x in BAD_SITES) else SiteRiskValues.safe

    @staticmethod
    def _get_site_classifications(categories):
        # TODO: @amihay current library doesn't return categories
        # use native Api
        return {}

    # TODO: handle other exception as well
    @retry(wait_exponential_multiplier=2, wait_exponential_max=1000, retry_on_exception=retry_if_api_limit)
    def _get_url_report(self, url, timeout):
        url_report = self.vt.get_url_report(this_url=url, timeout=timeout)
        if url_report['response_code'] == 204:  # api limier
            raise ApiLimitException()
        return url_report

    def _get(self, url, timeout=None, *args, **kwargs) -> UrlResult:
        url_report = self._get_url_report(url=url, timeout=timeout)
        domain_report = self.vt.get_domain_report(this_domain=url)
        site_voting = self._get_site_voting(url_report['results']['scans']) if 'scans' in url_report['results'] else None
        site_classfications = self._get_site_classifications(domain_report)
        url_result = UrlResult(url=url,
                               site_voting=site_voting,
                               site_risk=self._get_site_risks(site_voting),
                               site_classification=site_classfications)
        return url_result
