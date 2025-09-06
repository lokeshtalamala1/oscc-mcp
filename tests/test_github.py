import pytest
from backend.services.github_service import fetch_good_first_issues

@pytest.mark.asyncio
async def test_fetch_issues():
    issues = await fetch_good_first_issues()
    assert isinstance(issues, list)
