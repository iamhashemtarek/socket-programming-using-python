from socket import *

SERVER_ADDRESS = ('127.0.0.1', 8080)

client_socket = socket(AF_INET, SOCK_DGRAM)
try: 
        client_socket.sendto('DHCP req'.encode(), SERVER_ADDRESS)
        response, server_address = client_socket.recvfrom(1024)
        print(f'{response.decode()}')

except Exception as err:
    print('Error: ', err)
finally:
    client_socket.close()