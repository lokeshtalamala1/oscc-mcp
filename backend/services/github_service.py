import httpx
import os

GITHUB_ORG = os.getenv("GITHUB_ORG")
GITHUB_REPO = os.getenv("GITHUB_REPO")

async def fetch_good_first_issues():
    url = f"https://api.github.com/repos/{GITHUB_ORG}/{GITHUB_REPO}/issues"
    params = {"labels": "good first issue", "state": "open"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()
