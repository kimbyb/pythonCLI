import requests
from models import Commit

BASE_URL = "https://api.github.com"

def fetch_commits(owner: str, repo: str, limit: int = 30) -> list[Commit]:

    commits = []
    page = 1

    while len(commits) < limit:
        url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

        response = requests.get(url,  params={
                "per_page": 100,
                "page": page
            })

        response.raise_for_status()

        data = response.json()

        if not data:
            break

        for item in data:

            author = item["commit"]["author"]["name"]
            message = item["commit"]["message"]

            commits.append(Commit(author, message))

            if(len(commits) >= limit):
                break
        page += 1

    return commits