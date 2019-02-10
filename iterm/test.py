import subprocess
import os
import sys
import time
import websocket
try:
    import thread
except ImportError:
    import _thread as thread

def get_input():
    command = input("What is your command? ")
    return command

def on_message(ws, message):
    print("Message: %s" % message)
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
        for i in range(3):
            time.sleep(1)
            command = get_input()
            print('\n')
            ws.send(command)
        time.sleep(1)
        ws.close()

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",on_message =
            on_message, on_error = on_error, on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
