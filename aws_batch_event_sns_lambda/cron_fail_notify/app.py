import json
import os
import requests
import json
from loguru import logger


@logger.catch
def lambda_handler(event, context):
    msg_list = [event["Records"][i]["Sns"]["Message"] for i in range(len(event["Records"]))]
    detail = json.loads(msg_list[0])["detail"]

    rst = {
        "jobName": detail["jobName"],
        "jobId": detail["jobId"],
        "jobQueue": detail["jobQueue"],
        "status": detail["status"],
        "statusReason": detail["statusReason"],
    }
    json_rst = json.dumps({
        "text": str(rst),
    })
    webhookurl = os.environ["WebhookUrl"]
    # rst = requests.post(webhookurl, data=json_rst, headers={'Content-type': 'application/json'})
    # print(rst)

    return {
        'statusCode': 200,
        'body': json.dumps(str(rst))
    }
