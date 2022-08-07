import base64
import json
import os
import slack
from slack.errors import SlackApiError
from loguru import logger
from datetime import datetime, timedelta
import datetime as DT


# See https://api.slack.com/docs/token-types#bot for more info
BOT_ACCESS_TOKEN = "ggggggggggggggggggggg"
CHANNEL = "#budget"

slack_client = slack.WebClient(token=BOT_ACCESS_TOKEN)


@logger.catch
def sp_budget_notifier(data, context):
    start_time = datetime.combine(datetime.utcnow().date(), DT.time.min)
    now = datetime.utcnow()
    START_HOUR_1 = 1
    START_HOUR_2 = 10
    ok_hour = [START_HOUR_1, START_HOUR_2]

    ok_peroid_start_end = [(start_time + timedelta(hours=h, minutes=0), start_time + timedelta(hours=h, minutes=30)) for h in ok_hour]
    if not any([now > start and now < end for start, end in ok_peroid_start_end]):
        print("time period is not available: ", now)
        return

    pubsub_message = data

    # For more information, see
    # https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification_format
    try:
        notification_attr = json.dumps(pubsub_message["attributes"])
    except KeyError:
        notification_attr = "No attributes passed in"

    try:
        notification_data = base64.b64decode(data["data"]).decode("utf-8")
    except KeyError:
        notification_data = "No data passed in"

    # This is just a quick dump of the budget data (or an empty string)
    # You can modify and format the message to meet your needs
    budget_notification_text = f"{notification_attr}, {notification_data}"

    try:
        slack_client.api_call("chat.postMessage", json={"channel": CHANNEL, "text": budget_notification_text})
    except SlackApiError as e:
        logger.error("Error posting to Slack" + e)
