#!/usr/bin/env python3
import subprocess

commands = [
    "sudo apt install python3 -y",
    "sudo apt install python3-pip -y",
    "python3 -m pip install --user pipx",
]

def run_commands(commands):
    for command in commands:
        print(" ")
        print("[+] Installing ...")
        print(f"{command}")
        subprocess.run(command, shell=True)

run_commands(commands)
