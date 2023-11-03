import pytest
from src.applications.github.api.github_api import GitHubAPIClient


@pytest.fixture(scope="session")
def git_hub_api_app():
    # before each -- java
    # pre steps
    github_api_client = GitHubAPIClient()
    github_api_client.create_user()
    github_api_client.login()

    yield github_api_client # kind of return

    # after each -- java
    # post test steps
    github_api_client.remove_user()
    github_api_client.check_user_removed()
    github_api_client.more_cleaning()
    #####