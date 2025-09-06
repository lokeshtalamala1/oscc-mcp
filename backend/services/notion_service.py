import os
from notion_client import Client

notion = Client(auth=os.getenv("NOTION_TOKEN"))
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def create_notion_task(title: str, url: str):
    return notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties={
            "Name": {"title": [{"text": {"content": title}}]},
            "URL": {"url": url},
        },
    )
