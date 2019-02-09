import subprocess
import argparse
import os
import pty
import sys
import time


def main():
    command = input("Input your command: ")
    commands = command.split()
    subprocess.run(commands)
    commands = []

if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            print("\n")
            break
