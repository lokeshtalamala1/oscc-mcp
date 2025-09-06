import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_issue(issue: dict):
    title = issue.get("title", "")
    body = issue.get("body", "")
    # For demo: truncate body
    return {
        "title": title,
        "summary": (body[:200] + "...") if body else "",
        "url": issue.get("html_url")
    }
