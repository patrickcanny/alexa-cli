import boto3
import time
from config import SQS

# credentials to access SQS server
access_key = SQS.access_key
access_secret = SQS.access_secret
region = SQS.region
queue_url = SQS.queue_url

# method to pop messages off the SQS stack
# param: client - SQS client
# param: url - SQS server url
# returns: message
def pop_message(client, url):
    """Returns and deletes message message from SQS stack"""
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message

# Establishing the client using credentials
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

# Wait time before checking the SQS server
waittime = 20

# Setting SQS queue's wait time attribute
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})

# Get current time for start time
time_start = time.time()

# For 60 secs, check SQS for new messages every 20sec
while (time.time() - time_start < 60):
        print("Checking...")
        try:
                message = pop_message(client, queue_url)
                print(message)
                if message == "ls":
                        print("ls")
        except:
                pass
