#coding:utf-8

import paramiko
import time
import logging
import getpass

logging.basicConfig(level=logging.DEBUG)

ip = "10.10.10.228"
username = 'qianchen'
password = 'Huawei@456'

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname=ip, username=username, password=password, allow_agent=False, look_for_keys=False)
logging.debug('successfully connect to ' + ip)

command = sshclient.invoke_shell()
command.send("sys\n")
# command.send("inter loopback 2\n")
# command.send("ip add 44.44.44.4 255.255.255.255\n")

for n in range(10, 21):
    print("Creating vlan " + str(n) + ")\n")
    command.send("\n")
    command.send("vlan " + str(n) + "\n")
    command.send("descrption mytest_Vlan_test" + str(n) + "\n")
    command.send("name Vlan_test" + str(n) + "\n")
    command.send("quit\n")
    time.sleep(1)
command.send("commit\n")
command.send("disp vlan\n")
command.send("return\n")
command.send("save\n")
command.send("Y\n")

time.sleep(2)
output = command.recv(65535)
print(output.decode("ascii"))

sshclient.close()
