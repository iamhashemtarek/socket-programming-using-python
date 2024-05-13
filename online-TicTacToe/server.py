from tkinter import *
from tkinter import messagebox
from socket import *
from threading import *

#Functions
def checkWin():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text']  == board[i][2]['text']  != "":
            return board[i][0]['text']
        if board[0][i]['text']  == board[1][i]['text']  == board[2][i]['text']  != "":
            return board[0][i]['text']
    if board[0][0]['text']  == board[1][1]['text']  == board[2][2]['text']  != "":
        return board[0][0]['text']
    if board[0][2]['text']  == board[1][1]['text']  == board[2][0]['text']  != "":
        return board[0][2]['text']
    return False

def checkDraw():
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] == '':
                return False
    return True

def clickBoardBtn(row, col):
    global currentPlayer
    global clientSocket
    if board[row][col]['text'] == '':
        board[row][col]['text'] = currentPlayer
        clientSocket.sendall(f'{row},{col}'.encode())

    if checkWin():
        messagebox.showinfo(title='congrats', message=f'{checkWin()} win')
        toggleBtnState()
    elif checkDraw():
         messagebox.showinfo(title='Draw', message='no one win')
         toggleBtnState()
    else:
      pass
      #  currentPlayer = switchPlayer(currentPlayer)

def switchPlayer(player):
    if player == 'x':
        return 'y'
    else:
        return 'x'

def toggleBtnState():
    for row in range(3):
        for col in range(3):
            if board[row][col]['state'] ==  NORMAL:
                board[row][col]['state'] = DISABLED
            else:
                board[row][col]['state'] = NORMAL

def resetBoard(): 
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ''
    toggleBtnState()

def recvClick(clientSocket):
    global currentPlayer
    while True:
        try:
            clickData = clientSocket.recv(1024).decode()
            if not clickData:
                break
            row, col = map(int, clickData.split(',')) 
            currentPlayer = 'x'
            clickBoardBtn(row, col)
            currentPlayer = 'y'
        except Exception as err:
            print('Error: ', err)

    
#GUI
window = Tk()
window.title('Tic-Tac-Toe')

players = ['x', 'y']
currentPlayer = 'y'
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

header = Frame(window)
main = Frame(window)

header.pack()
main.pack()

label = Label(header, text=f'{currentPlayer} turn', font=('TKDefaultFont', 20), padx=5, pady=5)
restartBtn = Button(header, text='Restart', font=('TKDefaultFont', 20), padx=5, pady=5, command=resetBoard)
label.pack()
restartBtn.pack()

for row in range(3):
    for col in range(3):
        board[row][col] = Button(main, text="", width=8, height=4, font=('TKDefaultFont', 20), padx=5, pady=5, command=lambda row=row, col=col: clickBoardBtn(row, col))
        board[row][col].grid(row=row, column=col)


#socket 
SERVER_ADDRESS = ('127.0.0.1', 8080)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(SERVER_ADDRESS)
serverSocket.listen()
print(f'server is listening on {SERVER_ADDRESS}')

clientSocket, clientAddress = serverSocket.accept()
recvThread   = Thread(target=recvClick, args=((clientSocket,)))
recvThread.start()

window.mainloop()