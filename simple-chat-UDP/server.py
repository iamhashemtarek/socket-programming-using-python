from socket import *

SERVER_ADDRESS = ('127.0.0.1', 8080)

server_socket = socket(AF_INET, SOCK_DGRAM)

try: 
    server_socket.bind(SERVER_ADDRESS)

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f'received message from {client_address}: {message.decode()}')

        if message.decode().strip().lower() == 'quit':
            break

        response = input('response: ')
        server_socket.sendto(response.encode(), client_address)

except Exception as err:
    print('Error: ', err)
finally: 
    server_socket.close()