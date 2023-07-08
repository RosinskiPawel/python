from tkinter import *
import random

rand = random.randint(1, 3)


def wyniki(n):
    if rand == n:
        winText.pack(side="bottom")
    else:
        looseText.pack(side="bottom")


def delet():
    winText.pack_forget()
    looseText.pack_forget()


root = Tk()
root.geometry("350x350")
mainText = Label(text="Choose one number!", font="Courier", bd="10")
mainText.pack(side="top")
delButton = Button(root, text="Click me to play again!", command=delet).pack(side="top")
winText = Label(text="You Won!", font="Courier", bd="20")
looseText = Label(text="You loose!", font="Courier", bd="20")
btn = Button(root, text="ONE!", bd="20", command=lambda: wyniki(1))
btn.pack(side="left")
btn2 = Button(root, text="TWO!", bd="20", command=lambda: wyniki(2))
btn2.pack(side="left")
btn3 = Button(root, text="THREE!", bd="20", command=lambda: wyniki(3))
btn3.pack(side="left")

root.mainloop()
