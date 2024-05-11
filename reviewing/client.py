from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

SERVER_ADDRESS = ('127.0.0.1', 8080)

try:
    client_socket.connect(SERVER_ADDRESS)

    while True: 
        message = input('message: ')
        client_socket.sendall(message.encode())

        if message.strip().lower() == 'quit':
            break

        response = client_socket.recv(1024).decode()
        print(f'server: {response}')


except Exception as err:
    print('Error: ', err)
finally: 
    client_socket.close()