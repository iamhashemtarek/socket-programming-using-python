from socket import *

SERVER_HOST='127.0.0.1'
SERVER_PORT=8080

client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('message: ')
    encoded_message = message.encode()

    client_socket.sendto(encoded_message, (SERVER_HOST, SERVER_PORT))
    response, _ = client_socket.recvfrom(1024)
    decoded_response = response.decode()
    print(f'response: {decoded_response}')

    if encoded_message.strip().lower() == 'quit':
        break

client_socket.close()