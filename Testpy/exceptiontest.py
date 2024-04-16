import paramiko
import time
import getpass
import sys
import socket

username = 'qianchen'
password = 'Huawei@456'
ipfile = sys.argv[1]
cmdfile = sys.argv[2]

switch_with_auth_issue = []
switch_not_reachable = []

ip_list = open(ipfile, 'r')
for line in ip_list.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=username, allow_agent=False, password=password, look_for_keys=False)
        print('you have successfully connetct to ', ip)
        command = ssh_client.invoke_shell()
        cmdlist = open(cmdfile, 'r')
        cmdlist.seek(0)
        for line in cmdlist:
            command.send(line + "\n")
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535)
        print(output.decode('ascii'))
    except paramiko.AuthenticationException:
         print("User authentication failed for" + ip + ".")
         switch_with_auth_issue.append(ip)
    except socket.error:
         print("ip is not reachable for" + ip + ".")
         switch_not_reachable.append(ip)
    finally:
         print("haha ,now start info you ,keep warning")

ip_list.close()
ssh_client.close()

print("\nUser authentication failed for below switchs")
for i in switch_with_auth_issue:
    print(i)

print("\n failed connect below switchs, you should check network connect problem")
for i in switch_not_reachable:
    print(i)
