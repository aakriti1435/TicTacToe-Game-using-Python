from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
# root.iconbitmap("shy.ico")
root.resizable(0, 0)               # disabling window size
click = True


def close():
    root.destroy()
    # exit()


def reset():
    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""


button = StringVar()


def check(buttons):
    global click
    if buttons["text"] == "" and click == True:
        buttons["text"] = "X"
        click = False

    elif buttons["text"] == "" and click == False:
        buttons["text"] = "O"
        click = True

    win_method()


def win_method():
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or b4["text"] == "X" and b5["text"] == "X"
            and b6["text"] == "X" or b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or b1["text"] == "X"
            and b5["text"] == "X" and b9["text"] == "X" or b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"
            or b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or b2["text"] == "X" and b5["text"] == "X"
            and b8["text"] == "X" or b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        messagebox.showinfo("Winner X", "You have just win a game....\n CONGRATS :)")

    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or b4["text"] == "O" and b5["text"] == "O"
          and b6["text"] == "O" or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or b1["text"] == "O"
          and b5["text"] == "O" and b9["text"] == "O" or b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"
          or b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or b2["text"] == "O" and b5["text"] == "O"
          and b8["text"] == "O" or b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        messagebox.showinfo("Winner O", "You have just win a game....\n CONGRATS :)")


b1 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b1))
b2 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b2))
b3 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b3))
b4 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b4))
b5 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b5))
b6 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b6))
b7 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b7))
b8 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b8))
b9 = Button(root, text="", font="Arial 30 bold", height=1, width=3, command=lambda: check(b9))


b10 = Button(root, text="RESET GAME", font="Arial 10 bold", height=2, width=6, command=reset)
b11 = Button(root, text="EXIT GAME", font="Arial 10 bold", height=2, width=6, command=close)


b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)


b10.grid(row=4, column=0, columnspan=3, sticky=E+W)
b11.grid(row=5, column=0, columnspan=3, sticky=S+N+E+W)


root.mainloop()
