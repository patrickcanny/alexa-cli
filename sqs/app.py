import subprocess
import os
import sys
import time
import websocket
import queue_service as Q
import boto3
from config import SQS
try:
    import thread
except ImportError:
    import _thread as thread

access_key = SQS.access_key
access_secret = SQS.access_secret
region = SQS.region
queue_url = SQS.queue_url
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

def get_input():
    try:
        command = Q.pop_message(client, queue_url)
    except:
        print("Issue With Command")
        command = "pwd"
    return command

def on_message(ws, message):
    # print("Message: %s" % message)
    commands = message.split()
    try:
        subprocess.run(commands)
    except:
        print('Command Error')
    print('\n')

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(10):
            time.sleep(1)
            command = get_input()
            # print('\n')
            ws.send(command)
        time.sleep(1)
        ws.close()

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",on_message =
            on_message, on_error = on_error, on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
