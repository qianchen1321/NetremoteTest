#coding:utf-8

from netmiko import ConnectHandler

router2 = {
    'device_type' : 'cisco_ios',
    'ip': '10.10.10.206',
    'username': 'qianchen',
    'password':'cisco123'
}

connect = ConnectHandler(**router2)
print('sucessful connect ' + router2['ip'])
config_commands = ['int loopback 0', 'ip address 22.22.22.1 255.255.255.255']
output = connect.send_config_set(config_commands)
print(output)
result = connect.send_command('show run int loop 0')
print(result)
