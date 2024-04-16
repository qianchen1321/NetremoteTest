import telnetlib
import time
host = "6.6.6.6"
user = "qianchen"
password = "Huawei@456"

tn = telnetlib.Telnet(host)
matchUser_prompt = b"Username:"
matchPass_prompt = b"Password:"
changePassHint = b"The password needs to be changed. Change now? [Y/N]:"
tn.read_until(matchUser_prompt)
tn.write(user.encode('ascii')  + b"\n")
tn.read_until(matchPass_prompt)
tn.write(password.encode('ascii') + b"\n")
tn.read_until(changePassHint)
tn.write(b"N\n")
tn.write(b"sys\n")
tn.write(b"interface LoopBack 1\n")
tn.write(b"ip address 33.33.33.33 255.255.255.255\n")

#delay for waiting
time.sleep(0.5)
tn.write(b"quit\n")
Res = tn.write(b"dis curr\n")
print(Res)
#huawei can't use readall,must use read_very_eager
print(tn.read_very_eager().decode('ascii'))

#关闭连接
tn.close()
