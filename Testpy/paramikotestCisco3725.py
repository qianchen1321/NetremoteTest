#coding:utf-8

import paramiko
import time
import logging

logging.basicConfig(level=logging.DEBUG)

ip = "10.10.10.130"
username = 'qianchen'
password = 'cisco123'

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname=ip, username=username, password=password, allow_agent=False, look_for_keys=False)

logging.debug('successfully connect to ' + ip)

command = sshclient.invoke_shell()
command.send("config terminal\n")
command.send("inter loopback 2\n")
command.send("ip add 33.33.33.33 255.255.255.255\n")
command.send("end\n")
command.send("write mem\n")

time.sleep(2)
output = command.recv(65535)

print(output)

sshclient.close()
