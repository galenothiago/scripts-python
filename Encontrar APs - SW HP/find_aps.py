from netmiko import ConnectHandler


hp1 = {
'device_type': 'hp_comware',
'ip': '192.168.0.15',
'username': 'admin',
'password': 'admin',
}

hp2 = {
'device_type': 'hp_comware',
'ip': '192.168.1.30',
'username': 'admin',
'password': 'admin',
}

all_devices = [hp1, hp2]

#abre o arquivo que contem os ips e macs dos aps
macs_aps = open('ips_macs_aps.txt', 'r').readlines()


#primeiro laco e para testar as condicoes internas em cada um dos switches
for a_device in all_devices:
    try:
#abre conexao com o switch usando a biblioteca netmiko
        net_connect = ConnectHandler(**a_device)	

#segundo laco e para mandar os comandos usando a lista de ips e macs do aps em cada um dos swithces do primeiro laco
        for linha in macs_aps:
            valores = linha.split()
            commands1 = 'ping -c 3 ' + valores[0] + ''
            commands2 = 'display mac-address ' + valores[1] + ''
            output1 = net_connect.send_config_set(commands1, commands2)

        net_disconnect = net_connect.disconnect()

#mostra o erro que da caso nao consiga conexao com switch e pula para o proximo da iteracao       
    except Exception as e:
        print('Error: ') + str(e) + '\n'
        pass