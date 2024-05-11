from socket import *

SERVER_HOST='127.0.0.1'
SERVER_ADDRESS=8080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_ADDRESS))

try:
    while True:
        msg = input('enter a message: ')
        encoded_msg = msg.encode()

        client_socket.sendall(encoded_msg)

        if msg.strip().lower() == 'quit':
            break

        received_msg = client_socket.recv(1024)
        decoded_msg = received_msg.decode()
        print(f'server: {decoded_msg}')

        if decoded_msg.strip().lower() == 'quit':
            break
except Exception as err:
    print(f'error: {err}')       

client_socket.close()