#!/usr/bin/env python3
"""Tests for the GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value
        and get_json is called once with the correct URL."""
        # Arrange: Set a mock return value
        mock_get_json.return_value = {"login": org_name}

        # Act: Create client instance and call .org property
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert: .org returns the mock json and get_json called once with expected URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct value from org"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
