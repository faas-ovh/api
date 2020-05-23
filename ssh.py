# https://hackersandslackers.com/automate-ssh-scp-python-paramiko/

import paramiko
import json
from collections import namedtuple

import argparse

config = "..\\config\\faas.json"

str = open(config, "r").read()
dicts = json.loads(str)
for dict in dicts:
    print(dict)
    Server = namedtuple("Server", dict.keys())(*dict.values())
    # print( Server )
    print( Server.hostname )

# exit()
#
# class Server(object):
#     def __init__(self, hostname, username, password, *args, **kwargs):
#         self.hostname = hostname
#         self.username = username
#         self.password = password

# s = Server(cfg)
#
# commands = [
#     "pwd",
#     "id",
#     "uname -a",
#     "df -h"
# ]

# commands = [
#     "pwd",
#     "id",
#     "uname -a",
#     "df -h"
# ]


def commandList(commands):
    # execute the commands
    for command in commands:
        print("=" * 50, command, "=" * 50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)

def bashScript(filename):
    # read the BASH script content from the file
    bash_script = open(filename).read()
    # execute the BASH script
    stdin, stdout, stderr = client.exec_command(bash_script)
    # read the standard output and print it
    print(stdout.read().decode())
    # print errors if there are any
    err = stderr.read().decode()
    if err:
        print(err)


# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=Server.hostname, username=Server.username, password=Server.password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

commandList([
    "pwd",
    "id",
    "uname -a",
    "df -h"
])
bashScript("script.sh")

# close the connection
client.close()

