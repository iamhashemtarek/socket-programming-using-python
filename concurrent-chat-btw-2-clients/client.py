from socket import *
from threading import *

def send_message(client_socket):
    while True:
        try: 
            message = input('message: ')
            client_socket.sendall(message.encode())

            if message.strip().lower() == 'quit':
                break
        except Exception as err:
            print('Error: ', err)
            break


def recv_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)

            if message.strip().lower() == 'quit':
                break
        except Exception as err:
            print('Error: ', err)
            break

def main():
    SERVER_ADDRESS = ('127.0.0.1', 8080)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    send_thread = Thread(target=send_message, args=((client_socket, )))
    recv_thread = Thread(target=recv_message, args=((client_socket, )))

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

    client_socket.close()

if __name__ == '__main__':
    main()