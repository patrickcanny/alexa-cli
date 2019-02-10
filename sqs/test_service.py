import boto3
from config import SQS

# credentials to access SQS server
access_key = SQS.access_key
access_secret = SQS.access_secret
region = SQS.region
queue_url = SQS.queue_url

def post_message(client, message_body, url):
    response = client.send_message(QueueUrl = url, MessageBody= message_body)
    # print("post message:",response)

client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
post_message(client, "grep *.py", queue_url)
