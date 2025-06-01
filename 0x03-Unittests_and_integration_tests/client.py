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

    @staticmethod
    def has_license(repo, license_key):
        """Check if a repo has a specific license key."""
        return repo.get("license", {}).get("key") == license_key

    @property
    def org(self):
        """Return organization data from GitHub."""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self):
        return self.org["repos_url"]

    def public_repos(self):
        """Returns list of repository names"""
        return [repo["name"] for repo in get_json(self._public_repos_url)]

    def public_repos(self, license=None):
        """Returns a list of repository names. Can be filtered by license."""
        repos = get_json(self._public_repos_url)

        if license is None:
            return [repo["name"] for repo in repos]

        return [
            repo["name"]
            for repo in repos
            if repo.get("license", {}).get("key") == license
        ]
