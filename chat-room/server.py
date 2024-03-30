from threading import *
from socket import *

def handle_client(client_socket, client_address):
    print(f'connection from client {client_address}')

    while True:
        try:
            received_msg = client_socket.recv(1024)
            decoded_msg = received_msg.decode()

            if not received_msg:
                break

            print(f'client {client_address}: {decoded_msg}')

            for client in clients:
                if client != client_socket:
                    client.sendall(received_msg)

        except Exception as err:
            print(f'error: err')
            break
    
    print(f'connection with {client_address} is closed')
    client_socket.close()

HOST='127.0.0.1'
PORT=8080
clients = []

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'server is listening on port {PORT}')

while True:
    try:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        client_thread = Thread(target=handle_client, args=(client_socket, client_address))
        
        client_thread.start()
    except Exception as err:
        print(f'error: {err}')
        break

server_socket.close()