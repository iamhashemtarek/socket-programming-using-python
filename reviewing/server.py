from socket import *
from threading import *

clients = []

def handleClient(client_socket, client_address): 
    print(f'connection with {client_address} has been established')
    while True: 
        try: 
            message = client_socket.recv(1024).decode()
            for client in clients:
                if(client != client_socket):
                    client.sendall(message.encode())
            
            if message.strip().lower() == 'quit':
                break
        except Exception as err:
            print('Error:', err)

    clients.remove(client_socket)   
    print(f'client {client_address} disconnected')         

def main():
    SERVER_ADDRESS = ('127.0.0.1', 8080)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen()
    print(f'server is listening on {SERVER_ADDRESS}')
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            client_thread = Thread(target=handleClient, args=((client_socket, client_address)))

            client_thread.start()

        except Exception as err:
            print('Error: ', err)
            break
    server_socket.close()

if __name__ == '__main__':
    main()