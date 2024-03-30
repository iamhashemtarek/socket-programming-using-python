from threading import *
from socket import *

def send_messages(client_socket):
    while True:
        try:
            msg = input('message: ')
            encoded_msg = msg.encode()

            client_socket.sendall(encoded_msg)

            if msg.strip().lower() == 'quit':
                break

        except Exception as err:
            print(f'error: {err}')
            break

def receive_messages(client_socket, client_address):
    while True:
        try:
            received_msg = client_socket.recv(1024)
            decoded_msg = received_msg.decode()

            print(f'{client_address}: {decoded_msg}')


            if decoded_msg.strip().lower() == 'quit':
                break

        except Exception as err:
            print(f'error: {err}')
            break

def main():
    SERVER_ADDRESS='127.0.0.1'
    SERVER_PORT=8080

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_ADDRESS,SERVER_PORT))

    send_thread = Thread(target=send_messages, args=(client_socket,))
    receive_thread = Thread(target=receive_messages, args=(client_socket, client_socket.getpeername()))

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

    client_socket.close()

if __name__ == '__main__':
    main()