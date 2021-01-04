#!/usr/bin/env python
import argparse
import logging

from site_checker.api.models import UrlResult
from site_checker.api.run_server import run_server
from site_checker.api.site_checker import site_checker

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', '-d', type=str, help='path to data', required=False)
    args = parser.parse_args()

    if args.data_path:
        data = open(args.data_path).readlines()
        for item in data:
            result = site_checker(item)
            url_result = UrlResult(**result)
            print(f'Site {item} is {url_result.site_risk}')
        return

    run_server()


main()
