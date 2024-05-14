from socket import *
from threading import *
import tkinter as tk
from tkinter import scrolledtext

def send_message(client_socket):
    while True:
        try:
            ##pick message
            message = entry_field.get()
            print(message)
            if message:
              print(message)
              chat_box.insert(tk.END, "You: " + message + '\n')
              entry_field.delete(0, tk.END)
              client_socket.sendall(bytes(message, 'utf-8'))
            
            if message == 'quit':
                break

        except Exception as err: 
            print('Error: ', err)
            break

def recv_message(client_socket):
    while True:
        try:
            ##pick message
            message = client_socket.recv(1024).decode()
            if message:
                chat_box.insert(tk.END, "Friend: " + message + '\n')
            if message == 'quit':
                break
        except Exception as err: 
            print('Error: ', err)
            break



# Create the main window
root = tk.Tk()
root.title("Simple Chat App")

# Create a ScrolledText widget for displaying chat messages
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
chat_box.pack()

# Create an Entry widget for typing messages
entry_field = tk.Entry(root)
entry_field.pack(fill=tk.X, padx=10, pady=5)


# Create a button to send messages
send_button = tk.Button(root, text="Send", command=lambda : send_message(client_socket))
send_button.pack(pady=5)

SERVER_ADDRESS = ('127.0.0.1', 8080)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

send_thread = Thread(target=send_message, args=((client_socket,)))
recv_thread = Thread(target=recv_message, args=((client_socket,)))

send_thread.start()
recv_thread.start()

# send_thread.join()
# recv_thread.join()

root.mainloop()

