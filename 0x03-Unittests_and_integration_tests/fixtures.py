TEST_PAYLOAD = [
    (
        {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        },
        [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}},
        ],
        ["repo1", "repo2", "repo3"],
        ["repo1", "repo3"],
    ),
    # Add more test cases as needed
]

