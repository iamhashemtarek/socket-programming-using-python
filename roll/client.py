from threading import Thread
import random
from tkinter import *
from tkinter import messagebox

from socket import *

# global variables
player = 0  # indicate which player has to play (1 me , 0 other )
meScore = 0  # indicate which turn used to show if we finish game or not
oppositeScore = 0


def check():
    if meScore >= 100:
        win("Client")
    elif oppositeScore >= 100:
        win("Server")


def win(player):
    messagebox.showinfo("win", player + " is win")
    wind.destroy()


def clicked1():
    global player
    global meScore
    if (player == 1):
        player = 0  # make turn to other player
        # calulate rand value
        p = random.randint(0, 20)
        meScore += p
        sendPlay(p)
        check()


def sendPlay(p):
    showStatus("You played -{}\n Server Turn".format(p))
    # display
    lbMe["text"] = "Client:{}".format(meScore)
    n = str(meScore)
    n = n.encode()
    soc.send(n)


def handlePlay(n):
    global player
    global oppositeScore
    oppositeScore = n
    lbOpposite["text"] = "Server:{}".format(oppositeScore)
    player = 1
    check()


def applyPlay(p):
    showStatus("Your Turn")
    p = p.decode()
    p = int(p)
    handlePlay(p)


def showStatus(msg):
    lbStatus["text"] = msg


# window
wind = Tk()
wind.title("Dice Roll - Client")  # title
wind.geometry("450x450")  # size

# labels one and two players
lbMe = Label(wind, text="Me:100", font=('Arial', 18))
lbMe.grid(row=0, column=0)

lbOpposite = Label(wind, text="Opposite:100", font=('Arial', 19))
lbOpposite.grid(row=0, column=2)

lbStatus = Label(wind, text="Waiting", font=('Arial', 19))
lbStatus.grid(row=4, column=1)

btn1 = Button(wind, text="Roll", fg="black", width=10, bg="red",
              height=5, font='Arial', command=clicked1)
btn1.grid(row=2, column=1)


soc = socket(AF_INET, SOCK_STREAM)
showStatus("Waiting")


def connectServer():
    global soc
    soc.connect(("127.0.0.1", 6000))
    showStatus("Connected")
    t = Thread(target=rec)
    t.start()


def rec():
    while True:
        p = soc.recv(10)
        applyPlay(p)


tConnect = Thread(target=connectServer)
tConnect.start()


wind.mainloop()
