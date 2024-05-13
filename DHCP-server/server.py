from socket import *

SERVER_ADDRESS = ('127.0.0.1', 8080)

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)

print(f'udp server is listening on {SERVER_ADDRESS}')

while True:
    try:
        message, client_address = server_socket.recvfrom(1024)
        if client_address:
            print(f'connected to {client_address}')
        server_socket.sendto('assign ip xxx.xxx.xxx.xxx'.encode(), client_address)
    except Exception as err:
        print('Error: ', err)
        break

server_socket.close()
