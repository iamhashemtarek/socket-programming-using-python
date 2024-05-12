import tkinter as tk
from tkinter import messagebox

# Function to check for a win
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a draw
def check_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Function to handle button click
def button_click(row, col):
    global current_player

    if board[row][col] == "" and not winner:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_win():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)
    current_player = "X"
    winner = False

# Initialize variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
winner = False

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Create a reset button
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_game)
reset_button.grid(row=3, columnspan=3, padx=5, pady=10)

# Start the event loop
root.mainloop()
    