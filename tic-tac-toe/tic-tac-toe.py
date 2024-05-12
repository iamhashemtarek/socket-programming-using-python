from tkinter import *
from tkinter import messagebox
import random

def check_win():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text']  == board[i][2]['text']  != "":
            #board[i][0]['bg'] = board[i][1]['bg']  = board[i][2]['bg'] = 'red'
            return True
        if board[0][i]['text']  == board[1][i]['text']  == board[2][i]['text']  != "":
            return True
        
    if board[0][0]['text']  == board[1][1]['text']  == board[2][2]['text']  != "":
        return True
    if board[0][2]['text']  == board[1][1]['text']  == board[2][0]['text']  != "":
        return True
    return False

def check_draw():
    for row in board:
        for cell in row:
            if cell['text'] == '':
                return False
    return True

def button_click(row, col):
    global current_player
    if board[row][col]['text'] == '':
        board[row][col]['text'] = current_player

        if check_win():
            label.config(text=f'{current_player} wins')
            disable_buttons()
            messagebox.showinfo(title='congrats', message=f'winner is {current_player}')
        elif check_draw():
            label.config(text='Draw')
            disable_buttons()
        else:
            if current_player == players[0]:
                current_player = players[1]
            else:
                current_player = players[0]
            label.config(text=f'{current_player} turn')

def reset_game():
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ''
    label.config(text=f'{random.choice(players)} turn')
    enable_buttons()

def disable_buttons():
    for row in range(3):
        for col in range(3):
            board[row][col].config(state=DISABLED)

def enable_buttons():
    for row in range(3):
        for col in range(3):
            board[row][col].config(state=NORMAL)
            
#logic
window = Tk()
window.title('tic-tac-toe')

players = ['x', 'y']
current_player = random.choice(players)

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

header = Frame(window, padx=5, pady=5)
main = Frame(window, padx=5, pady=5)

header.pack()
main.pack()

#header
label =  Label(header,  text=f'{current_player} turn', font=('TKDefaultFont', 40), padx=5, pady=5)
restart_button = Button(header, text='restart',font=('TKDefaultFont', 20), padx=5, pady=5, command=reset_game)
label.pack()
restart_button.pack()

#main
for row in range(3):
    for col in range(3):
        board[row][col] = Button(main, text= '',font=('TKDefaultFont', 20), width=8,  height=4, padx=5, pady=5, command=lambda row=row, col=col : button_click(row, col))
        board[row][col].grid(row=row, column=col)

window.mainloop()