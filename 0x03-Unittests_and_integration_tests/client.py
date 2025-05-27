#!/usr/bin/env python3
"""GithubOrgClient module."""

import requests


def get_json(url):
    """GET JSON data from a URL."""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Github organization client."""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Return organization data from GitHub."""
        return get_json(self.ORG_URL.format(self.org_name))
