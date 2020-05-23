# https://hackersandslackers.com/automate-ssh-scp-python-paramiko/

import paramiko
import json
from collections import namedtuple

config = "..\\config\\faas.json"

str = open(config, "r").read()
dict = json.loads(str)
Server = namedtuple("Server", dict.keys())(*dict.values())

print( Server )
print( Server.hostname )
print( type(Server) )

# exit()
#
# class Server(object):
#     def __init__(self, hostname, username, password, *args, **kwargs):
#         self.hostname = hostname
#         self.username = username
#         self.password = password

# s = Server(cfg)

commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
]

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=Server.hostname, username=Server.username, password=Server.password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# execute the commands
for command in commands:
    print("=" * 50, command, "=" * 50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

client.close()
