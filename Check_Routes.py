
from netmiko import ConnectHandler
from easygui import passwordbox


password = passwordbox('Password Please: ')

DMVPN = {
    'device_type': 'cisco_ios',
    'ip': '10.212.32.26',
    'username': 'LA_PAM_01',
}

DMVPN['password'] = password

net_connect = ConnectHandler(**DMVPN)

vrfs = ["AWS_CP_PRD","AWS_CP_QA","AWS_CP_SIT","AWS_CP_STG","AWS_DOT_PRD","AWS_DOT_SIT","AWS_DOT_STG","AWS_GEN_PRD","AWS_GEN_QA1","AWS_GEN_QA2","AWS_GEN_SIT","AWS_GEN_STG","MARPLE_AWS"]

for vrf in vrfs:
    command = "show ip route vrf " + vrf
    output = net_connect.send_command(command)

    print output

