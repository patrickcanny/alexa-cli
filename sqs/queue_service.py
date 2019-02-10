import boto3
from config import SQS

# credentials to access SQS server
access_key = SQS.access_key
access_secret = SQS.access_secret
region = SQS.region
queue_url = SQS.queue_url
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

def post_message(client, message_body, url):
    response = client.send_message(QueueUrl = url, MessageBody= message_body)
    # print("post message:",response)

def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)
    # print("pop message:",response)
    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
