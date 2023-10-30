from src.applications.github.api.github_api import GitHubAPIClient


def test_search_for_existing_repo():
    github_api_client = GitHubAPIClient()

    existing_repo_name = 'sergii'
    repos = github_api_client.search_repos(existing_repo_name) # list/array returned

    print("Checking total count is not 0")
    
    assert repos['total_count'] != 0  # some elements exists in array/list


def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    
    nonexisting_repo_name = 'lnasdklfnkjanskdjfnkjabsdjhfuyagsuygfuyagsduyfgauysdf'
    repos = github_api_client.search_repos(nonexisting_repo_name) # list/array returned

    print("Checking total count is 0")
    
    assert repos['total_count'] == 0  # some elements exists in array/list


def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    
    nonexisting_commit_hasg = 'lnasdklfnkjanskdjfnkjabsdjhfuyagsuygfuyagsduyfgauysdf'
    repos = github_api_client.search_commits(nonexisting_commit_hasg) # list/array returned

    print("Checking total count is 0")
    
    assert 0 == 0  # some elements exists in array/list
