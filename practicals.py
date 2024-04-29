# Server configurations dictionary
# 键是服务器名称，值是一个字典，包含了服务器的 IP 地址、端口和状态

server_config={
    'server1':{'ip':'192.168.1.1','port':8080,'status':'active'},
    'server2':{'ip':'192.168.1.2','port':8000,'status':'inactive'},
    'server3':{'ip':'192.168.1.3','port':9000,'status':'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name,{}).get('status','Server not found')
def get_server_ip(server_name):
    return server_config.get(server_name,{}).get('ip','Server not found')
def get_server_port(server_name):
    return server_config.get(server_name,{}).get('port','Server not found')

server_name=input('server1 server2 server3\n')

status=get_server_status(server_name)
ip=get_server_ip(server_name)
port=get_server_port(server_name)

print(f"status: {status}\nip: {ip}\nport: {port}\n")
