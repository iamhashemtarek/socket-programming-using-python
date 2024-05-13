# client.py
import socket
import tkinter as tk
from tkinter import messagebox, simpledialog
import threading

HOST = '127.0.0.1'
PORT = 65432

def send_choice(choice):
    try:
        client_socket.send(choice.encode())
    except Exception as e:
        print("Error sending choice:", e)

def receive_messages():
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            if data == "Game over.":
                messagebox.showinfo("Game Over", "All rounds played. Game over.")
                break
            else:
                if "Winner:" in data:
                    messagebox.showinfo("Round Winner", data)
                else:
                    chat_box.insert(tk.END, data + '\n')
                    chat_box.see(tk.END)
    except Exception as e:
        print("Error receiving message:", e)

def connect_to_server(name, num_rounds):
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("Connected to server")
        client_socket.send(name.encode())
        print("Sent player name:", name)
        client_socket.send(num_rounds.encode())
        print("Sent number of rounds:", num_rounds)
        threading.Thread(target=receive_messages).start()
    except Exception as e:
        print("Error connecting to server:", e)

def on_closing():
    send_choice("QUIT")
    client_socket.close()
    root.quit()

def start_game():
    name = simpledialog.askstring("Name", "Enter your name:")
    num_rounds = simpledialog.askinteger("Number of Rounds", "Enter the number of rounds:")
    connect_to_server(name, str(num_rounds))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock Paper Scissors")

    start_game_button = tk.Button(root, text="Start Game", command=start_game)
    start_game_button.pack(pady=20)

    root.mainloop()
