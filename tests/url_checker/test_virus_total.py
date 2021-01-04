from site_checker.api.models import SiteRiskValues
from site_checker.url_checker.virus_total import VirusTotalChecker


def test_get():
    vt = VirusTotalChecker(api_key='2947ac8a6fe1e5eac4845b606f0c69ea0c85b892f062667197b4fb78e00a2ae7')
    vt.get('not exists')


def test_get_site_voting():
    voting = {
        "CMC Threat Intelligence": {
            "detected": True,
            "result": "phishing site"
        },
        "CLEAN MX": {
            "detected": False,
            "result": "clean site"
        },
        "DNS8": {
            "detected": False,
            "result": "clean site"
        },
        "NotMining": {
            "detected": False,
            "result": "unrated site"
        },
    }

    actual = VirusTotalChecker._get_site_voting(voting)
    expected = {'phishing': 1, 'unrated': 1, 'clean': 2}
    assert sorted(actual.items()) == sorted(expected.items())


def test_get_site_risk():
    site_voting = {'phishing':4}
    actual = VirusTotalChecker._get_site_risks(site_voting)
    expected = SiteRiskValues.risk
    assert actual == expected
