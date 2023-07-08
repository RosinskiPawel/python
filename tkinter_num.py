# import easygui as gui
# import random

# while True:
#     rand = random.randint(0, 2)
#     if (
#         gui.indexbox(
#             msg="wybierz jedną liczbę",
#             title="GRA 1 z 3",
#             choices=("1", "2", "3"),
#         )
#         == rand
#     ):
#         gui.msgbox(msg="Trafiłeś. Brawo!", ok_button="OK")
#     else:
#         gui.msgbox(msg=f"Nie tym razem. Wylosowano: {rand}", ok_button="OK")
#     if gui.indexbox(msg="Chcesz zagrać ponownie?", choices=("TAK", "NIE")) == 1:
#         break


# 1. losowanie pap, kam czy noz
# 2. potem pyt o wybranie pap, kam czy noz
# 3. porownanie wylosowanego z wybranym
# 4. wynik
# 5. pyt o kontynuacje

# import tkinter as tk

# # window = tk.Tk()
# # frame = tk.Frame(master=window, relief="solid")

# # greets = tk.Label(
# #     master=frame,
# #     text="Hallo Sralo",
# #     font="Courier",
# #     foreground="white",
# #     background="green",
# # )
# # button = tk.Button(text="ONE", bg="red", fg="yellow")
# # entry = tk.Entry()
# # name = entry.get()
# # frame.pack()
# # greets.pack()
# # entry.pack()
# # button.pack()

# window.mainloop()

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
