import requests
from app.config import GITHUB_TOKEN

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_repo_structure(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    res = requests.get(url, headers=HEADERS)
    res.raise_for_status()
    return res.json()

