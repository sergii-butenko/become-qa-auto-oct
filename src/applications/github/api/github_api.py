import requests


class GitHubAPIClient:
    """Current class contains every API call we use in tests"""
    
    def __init__(self) -> None:
        pass

    def search_repos(self, repo_name):
        print("Sending request to url https://api.github.com/search/repositories")
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})
        print(f"Responce retriewed {r}")

        body = r.json()

        return body
    

    def search_commits(self, commit_hash):
        print("Sending request to url https://api.github.com/search/commit")
        r = requests.get("https://api.github.com/search/commit", params={'q': commit_hash})
        print(f"Responce retriewed {r}")

        body = r.json()

        return body
    