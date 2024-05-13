from socket import *
from datetime import *

SERVER_ADDRESS = ('127.0.0.1', 8080)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen()

print(f'server is  listening on {SERVER_ADDRESS}')

while True:
    try:
        client_socket, client_address = server_socket.accept()
        current_time = datetime.now()
        client_socket.sendall(f'{current_time}'.encode())
    except Exception as err:
        print('Error: ', err)
        break
    finally:
        client_socket.close()
        print(f'client {client_address} disconnected')

server_socket.close()