import subprocess
import os

def main():
    commands = []
    commands.append(input("Input your command: "))
    subprocess.run(commands)
    commands = []

if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            print("\n")
            break
