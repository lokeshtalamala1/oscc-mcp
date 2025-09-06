from fastapi import FastAPI
from services.github_service import fetch_good_first_issues
from services.notion_service import create_notion_task
from services.slack_service import post_to_slack
from services.auth_service import validate_user
from services.summarizer import summarize_issue
from utils.logger import logger

app = FastAPI(title="Open Source Contribution Companion")

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to OSCC API"}

@app.get("/issues/")
async def get_issues():
    issues = await fetch_good_first_issues()
    summaries = [summarize_issue(issue) for issue in issues]
    return {"issues": summaries}

@app.post("/notion/")
async def add_to_notion(title: str, url: str):
    task = await create_notion_task(title, url)
    logger.info(f"Task created in Notion: {title}")
    return {"status": "Task created", "task": task}

@app.post("/slack/")
async def send_slack(title: str, url: str):
    res = await post_to_slack(title, url)
    logger.info(f"Posted to Slack: {title}")
    return {"status": "Posted to Slack", "response": res}
