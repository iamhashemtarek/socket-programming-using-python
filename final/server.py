from socket import *
from threading import *

SERVER_ADDRESS = ('127.0.0.1', 8000)
clients = []

def handle_client(client_socket, client_address):
    print(f'connection with {client_address} has been established')

    while True:
        message = client_socket.recv(1024)

        for client in clients:
            if client != client_socket:
                client.sendall(f'{client_address}: {message.decode()}'.encode())
        
        if message.decode() == 'quit':
            break
    clients.remove(client_socket)
    client_socket.close()

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen()
        print(f'server is listening on {SERVER_ADDRESS}')

        while len(clients) <= 2:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)

            handle_client_thread = Thread(target=handle_client, args=((client_socket, client_address)))

            handle_client_thread.start()
            # handle_client_thread.join()
    except Exception as err:
        print(err)
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()