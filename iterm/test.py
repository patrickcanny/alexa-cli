import argparse
import subprocess
import os
import pty
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
    commands = [message]
    subprocess.run(commands)
    ws.close()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        command = get_input()
        ws.send(command)

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",on_message =
            on_message, on_error = on_error, on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()

# parser = argparse.ArgumentParser()
# parser.add_argument('-a', dest='append', action='store_true')
# parser.add_argument('-p', dest='use_python', action='store_true')
# parser.add_argument('filename', nargs='?', default='typescript_2')
# options = parser.parse_args()
# filename = options.filename
# mode = 'ab' if options.append else 'wb'



# # pty stuff
# with open(filename, mode) as script:
#     print('Script started, file is',filename)
#     script.write(('Script started on %s\n' % time.asctime()).encode())
#     ws = create_connection('ws://echo.websocket.org/')
#     ws.send('bash-3.2$ echo "Hello, World"\n')
#     pty.spawn(shell, read)
#     script.write(('Script done on %s\n' % time.asctime()).encode())
#     print('Script done, file is', filename)
