from netmiko import ConnectHandler


hp01 = {
'device_type': 'hp_comware',
'ip': '192.168.0.15',
'username': 'admin',
'password': 'admin',
'blocking_timeout': 16,
}

hp02 = {
'device_type': 'hp_comware',
'ip': '192.168.1.20',
'username': 'admin',
'password': 'admin',
'blocking_timeout': 16,
}

all_devices = [hp01, hp02]

#abre o arquivo que contem o range de portas em cada switch a ser configurado
port_vlan = open('portas_switch.txt', 'r').readlines()

#primeiro laco e para testar as condicoes internas em cada um dos switches
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)

    try:
#abre conexao com o switch usando a biblioteca netmiko
#segundo laco e para mandar os comandos usando a lista de ips e macs do aps em cada um dos swithces do primeiro laco
        for l in port_vlan:
	    commands0 = 'vlan 3000' + ' '
	    commands1 = 'int range ' + l + ' port access vlan 300 ' + ' '
	    commands2 = 'quit'
	    output0 = net_connect.send_config_set(commands0)
    
#mostra o erro que da caso nao consiga conexao com switch e pula para o proximo da iteracao       
    except Exception as e:
        print ('Error: ') + str(e) + '\n'
        pass

    net_disconnect = net_connect.disconnect()
