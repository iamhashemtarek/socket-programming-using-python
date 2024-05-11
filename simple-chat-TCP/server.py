from socket import *

HOST = '127.0.0.1'
PORT = 8080

server_socket = socket(AF_INET, SOCK_STREAM)

try: 
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    print(f'server is listening on port {PORT}')

    client_socket, client_address = server_socket.accept()
    print(f'connection from {client_address} has been established')

    while True: 
        message = client_socket.recv(1024).decode()
        print(f'client: {message}')

        if message.strip().lower() == 'quit':
            break

        response = input('response: ')
        client_socket.sendall(response.encode())

except Exception as err:
    print('Error: ', err)

finally:
    client_socket.close()
    server_socket.close()
