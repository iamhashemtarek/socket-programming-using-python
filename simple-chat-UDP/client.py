from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)

SERVER_ADDRESS = ('127.0.0.1', 8080)
try: 
    while True: 
        message = input('message: ')
        client_socket.sendto(message.encode(), SERVER_ADDRESS)

        if message.strip().lower() == 'quit':
            break
        
        response, server_address = client_socket.recvfrom(1024)
        print(f'received message from {server_address}: {response.decode()}')

except Exception as err:
    print('Error: ', err)
finally:
    client_socket.close()