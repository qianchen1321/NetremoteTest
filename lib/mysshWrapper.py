# coding:utf-8

import paramiko
import socket


class MySSHclient(object):
    sshclient = paramiko.SSHClient()
    #初始化ssh 连接对象
    def __init__(self, host=None, port=22, username=None, password=None, \
                 pkey=None, key_filename=None, timeout=None, allow_agent=True, \
                 look_for_keys=True, compress=False):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.pkey = pkey
        self.key_filename = key_filename
        self.timeout = timeout
        self.allow_agent = allow_agent
        self.look_for_keys = look_for_keys
        self.compress = compress

    def connect_pass(self):
        try:
            MySSHclient.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            MySSHclient.sshclient.connect(hostname=self.host, port=self.port, username=self.username,
                                          password=self.password)
            return "SuccessConnect"
        except paramiko.AuthenticationException:
            print("User authentication failed for" + self.host + ".")
            return "AuthException"
        except socket.error:
            print("ip is not reachable for" + self.host + ".")
            return "SocketException"
        else:
            print("otherException ,keep warning")
            return "otherException"

    def connect_pkey(self):
        try:
            pkey = paramiko.RSAKey.from_private_key_file(self.key_filename)
            MySSHclient.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            MySSHclient.sshclient.connect(hostname=self.host, port=self.port, username=self.username, pkey=pkey)
            return "SuccessConnect"
        except paramiko.AuthenticationException:
            print("User authentication failed for" + self.host + ".")
            return "AuthException"
        except socket.error:
            print("ip is not reachable for" + self.host + ".")
            return "SocketException"
        else:
            print("otherException ,keep warning")
            return "otherException"


    def exec_Command(self, cmd=None):
        stdin, stdout, stderr = MySSHclient.sshclient.exec_command(cmd)
        stderrlines = stderr.readlines()
        print(stderrlines)
        stdoutlines = stdout.readlines()
        print(stdoutlines)        # stdinlines = stdin.readlines()
        # print(stdinlines)
        return (stdin, stdout, stderr)

    def upload_file(self, localfile, remotefile):
        sftpcli = paramiko.SFTPClient.from_transport(MySSHclient.sshclient.get_transport())
        sftpcli.put(localfile, remotefile)

    def close(self):
        MySSHclient.sshclient.close()


