# https://hackersandslackers.com/automate-ssh-scp-python-paramiko/

import paramiko
import json
from collections import namedtuple

import argparse


def commandList(commands, client):
    # execute the commands
    for command in commands:
        print("=" * 50, command, "=" * 50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)


def bashScript(filename, client):
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


def connect(Server):
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=Server.ip, username=Server.username, password=Server.password)
        return client
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()


def execScript(client, script):
    # commandList(["pkill apt"], client)
    # commandList(["apt-get install git"], client)

    bashScript(script, client)

    # close the connection
    client.close()


def getClient(hostname, config):
    str = open(config, "r").read()
    dicts = json.loads(str)
    for dict in dicts:
        # print(dict)
        Server = namedtuple("Server", dict.keys())(*dict.values())
        print(Server.ip, Server.hostname, Server.os)
        if Server.hostname == hostname:
            print(Server)
            return connect(Server)


client = getClient("1.faas.ovh", "..\\config\\faas.json")
# execScript(client, "apt.sh")
# execScript(client, "git.sh")
# execScript(client, "git-user.sh")
# execScript(client, "promagen/install.sh")
# execScript(client, "promagen/start.sh")
execScript(client, "promagen/stop.sh")
# execScript(client, "promagen/update.sh")

# s = Server(cfg)
#
# commands = [
#     "pwd",
#     "id",
#     "uname -a",
#     "df -h"
# ]
