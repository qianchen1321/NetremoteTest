import paramiko
import time
import getpass
import sys
import socket

username = 'qianchen'
# password = 'Huawei@456'
ipfile = sys.argv[1]

ip_list = open(ipfile, 'r')
for line in ip_list.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        if ip in ['10.10.10.130', '10.10.10.132']:
            ssh_client.connect(hostname=ip, username=username, password='cisco123', allow_agent=False,
                               look_for_keys=False)
            print('you have successfully connetct to ', ip)
            command = ssh_client.invoke_shell()
            command.send("enable\n")
            time.sleep(1)
            command.send("cisco123\n")
            time.sleep(1)
            command.send("config terminal\n")
            time.sleep(1)
            command.send("ip ftp username root\n")
            command.send("ip ftp password cisco123\n")
            command.send("file prompt quiet\n")
            command.send("end\n")
            command.send("copy running-config ftp://10.10.10.25\n")
            time.sleep(5)

        elif ip in ['10.10.10.133', '10.10.10.134', '10.10.10.135', '10.10.10.136']:
            print("please check huawei command")
            ssh_client.connect(hostname=ip, username=username, password='Huawei@456', allow_agent=False,
                               look_for_keys=False)
            print('you have successfully connetct to ', ip)
            command = ssh_client.invoke_shell()

            command.send("ftp 10.10.10.25\n")
            time.sleep(1)
            command.send("root\n")
            time.sleep(1)
            command.send("cisco123\n")
            time.sleep(1)
            command.send("bin\n")
            time.sleep(1)
            command.send("put vrpcfg.zip " + ip + "_vrpcfg.zip" + "\n")
            time.sleep(1)
            command.send("quit\n")
        else:
            print("no include manufactor,out")
            continue

        output = command.recv(65535)
        print(output.decode("ascii"))



    except paramiko.AuthenticationException:
        print("User authentication failed for" + ip + "")
    except socket.error:
         print("ip is not reachable for" + ip + ".")




ip_list.close()
ssh_client.close()

# print("\nUser authentication failed for below switchs")
# for i in switch_with_auth_issue:
#     print(i)
#
# print("\n failed connect below switchs, you should check network connect problem")
# for i in switch_not_reachable:
#     print(i)
