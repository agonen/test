from dataclasses import dataclass


class SiteRiskValues:
    risk = 'risk'
    safe = 'safe'


@dataclass
class UrlResult:
    url: str = None
    site_risk: SiteRiskValues = None
    site_voting: dict = None
    site_classification: dict = None
