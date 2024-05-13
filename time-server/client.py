from socket import *

SERVER_ADDRESS = ('127.0.0.1', 8080)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

current_time = client_socket.recv(1024).decode()

print(f'current time: {current_time}')

client_socket.close()