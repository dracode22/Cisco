
from netmiko import ConnectHandler
from easygui import passwordbox


password = passwordbox('Password Please: ')

Router = {
    'device_type': 'cisco_ios',
    'ip': '1.2.3.5',
    'username': 'Cisco',
}

Router['password'] = password

net_connect = ConnectHandler(**Router)

vrfs = ["Default"]

for vrf in vrfs:
    command = "show ip route vrf " + vrf
    output = net_connect.send_command(command)

    print output

