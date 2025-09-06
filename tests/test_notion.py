import pytest
from backend.services.notion_service import create_notion_task

@pytest.mark.asyncio
async def test_create_task(monkeypatch):
    async def fake_task(title, url):
        return {"id": "123", "title": title}
    monkeypatch.setattr("backend.services.notion_service.create_notion_task", fake_task)
    result = await create_notion_task("Test", "http://example.com")
    assert result["title"] == "Test"
