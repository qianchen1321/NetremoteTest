#coding:utf-8

from netmiko import ConnectHandler

router2 = {
    'device_type' : 'huawei',
    'ip': '10.10.10.219',
    'username': 'qianchen',
    'password':'Huawei@456'
}

connect = ConnectHandler(**router2)
print('sucessful connect ' + router2['ip'])
enable_output = connect.send_command(command_string='sys', expect_string='<HUAWEI>', read_timeout=20, cmd_verify=False)
print(enable_output)
# enable_output2 = connect.send_command('sys')
# print(enable_output2)

config_commands = ['int loopback 1', 'ip address 22.22.22.2 255.255.255.255']
#output = connect.send_multiline(config_commands, read_timeout=20, cmd_verify=False)
#print(output)
result = connect.send_command('disp cur', cmd_verify=False)
print(result)
