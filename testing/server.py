# server.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clients = {}
rounds_played = 0

def handle_client(conn, addr, player_name):
    global rounds_played
    conn.send("Welcome to Rock Paper Scissors!\n".encode())
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == "QUIT":
            conn.close()
            del clients[player_name]
            print(f"{player_name} disconnected.")
            break
        print(f"{player_name}: {data}")
        for client_name, client_conn in clients.items():
            if client_name != player_name:
                client_conn.send(f"{player_name}: {data}".encode())
    rounds_played += 1

    if rounds_played == len(clients) * int(num_rounds):
        print("All rounds played. Game over.")
        for client_conn in clients.values():
            client_conn.send("Game over.".encode())

def accept_clients():
    while True:
        conn, addr = server.accept()
        player_name = conn.recv(1024).decode()
        clients[player_name] = conn
        print(f"{player_name} connected from {addr}.")
        threading.Thread(target=handle_client, args=(conn, addr, player_name)).start()

def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server started on {HOST}:{PORT}")
    accept_clients()

if __name__ == "__main__":
    num_rounds = input("Enter number of rounds: ")
    start_server()
