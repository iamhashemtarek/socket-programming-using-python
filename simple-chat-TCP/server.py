from socket import *

HOST='127.0.0.1'
PORT=8080

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'server is listening on port {PORT}')


while True:
    client_socket, client_address = server_socket.accept()
    
    try:
        while True:
            received_message = client_socket.recv(1024)
            decoded_message = received_message.decode()

            print(f'client: {decoded_message}')

            if decoded_message.strip().lower() == 'quit':
                break

            msg = input('enter a message: ')
            encoded_msg = msg.encode()
            client_socket.sendall(encoded_msg)

            if encoded_msg.strip().lower() == 'quit':
                break


    except Exception as err:
        print(f'error: {err}')
    finally:
        print(f'connection with {client_address} is closed')
        client_socket.close()

# unreachable line
server_socket.close()