import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from utils.logger import logger

slack_token = os.getenv("SLACK_BOT_TOKEN")
slack_channel = os.getenv("SLACK_CHANNEL", "#general")
client = WebClient(token=slack_token)

async def post_to_slack(title: str, url: str):
    """Posts a message about an issue to Slack channel"""
    try:
        response = client.chat_postMessage(
            channel=slack_channel, 
            text=f"New Open Source Issue: *{title}*\n{url}"
        )
        logger.info(f"Posted issue to Slack: {title}")
        return response
    except SlackApiError as e:
        logger.error(f"Slack API Error: {e.response['error']}")
        return {"error": str(e)}
