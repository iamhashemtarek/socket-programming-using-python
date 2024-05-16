from threading import Thread
import random
from tkinter import *
from tkinter import messagebox

from socket import *

# global variables
player = 0  # indicate which player has to play (1 me , 0 other )
meScore = 0  # indicate which turn used to show if we finish game or not
oppositeScore = 0


# check who is winner
def check():
    if meScore >= 100:
        win("Server")
    elif oppositeScore >= 100:
        win("Client")


def win(player):
    messagebox.showinfo("win", player + " is win")
    wind.destroy()


def clicked1():
    global player
    global meScore
    if (player == 1):
        player = 0  # make turn to other player
        p = random.randint(0, 20)
        meScore += p
        sendPlay(p)
        check()


def sendPlay(p):
    showStatus("You played -{}\n Opposite Turn".format(p))
    # display
    lbMe["text"] = "Server:{}".format(meScore)
    n = str(meScore)
    n = n.encode()
    c.send(n)


def handlePlay(n):
    global player
    global oppositeScore
    oppositeScore = n
    lbClient["text"] = "Client:{}".format(oppositeScore)
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
wind.title("Dice Roll - Server")
wind.geometry("450x450")


# labels one and two players
lbMe = Label(wind, text="Me: 0", font=('Arial', 18))
lbMe.grid(row=0, column=0)

lbClient = Label(wind, text="Opposite: 0", font=('Arial', 18))
lbClient.grid(row=0, column=2)

lbStatus = Label(wind, text="Waiting", font=('Arial', 18))
lbStatus.grid(row=2, column=1)

btn1 = Button(wind, text="Roll", fg="black", width=10, bg="green",
              height=5, font='Arial', command=clicked1)
btn1.grid(row=1, column=1)

# session with server
soc = socket(AF_INET, SOCK_STREAM)
soc.bind(("127.0.0.1", 6000))
soc.listen(5)
c = None


def handleClient():
    global player
    global c
    player = 1
    c, ad = soc.accept()
    showStatus(" a player connected\n Your Turn")
    t = Thread(target=rec, args=[c, ])
    t.start()


def rec(c):
    while True:
        p = c.recv(10)
        applyPlay(p)


acc = Thread(target=handleClient)
acc.start()

showStatus("waiting....")

wind.mainloop()
