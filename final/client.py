from socket import *
from threading import *

SERVER_ADDRESS = ('127.0.0.1', 8000)

def send_msg(client_socket):
    while True:
        message = input('message: ')
        print(f'me: {message}')
        client_socket.sendall(message.encode())
        if message == 'quit':
            break

def recv_msg(client_socket):
    while True:
        response = client_socket.recv(1024)
        print(response.decode())
        if response.decode() == 'quit':
            break

def main():
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(SERVER_ADDRESS)

        send_msg_thread = Thread(target=send_msg, args=((client_socket,)))
        recv_msg_thread = Thread(target=recv_msg, args=((client_socket,)))

        send_msg_thread.start()
        recv_msg_thread.start()

        send_msg_thread.join()
        recv_msg_thread.join()

        client_socket.close()

    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()