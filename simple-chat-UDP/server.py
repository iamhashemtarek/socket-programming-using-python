from socket import *

HOST='127.0.0.1'
PORT=8080

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((HOST,PORT))

print(f'server is listening on port {PORT}')

while True:
    message, client_address = server_socket.recvfrom(1024)
    decoded_message = message.decode()

    print(f'client {client_address}: {decoded_message}')
    
    server_socket.sendto(message, client_address)

    if decoded_message.strip().lower() == 'quit':
        break

server_socket.close()
    