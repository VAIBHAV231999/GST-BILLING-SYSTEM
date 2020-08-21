from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import os

from tkinter import Text, Tk

firstw = Tk()
firstw.title("GST BILLING SYSTEM")
firstw.geometry("1600x1000+0+0")
label = Label(text="GST BILLING SYSTEM", font=("times new roman", 35), bg="MediumOrchid2")
label.pack(side=TOP, fill=X)
user1 = Label(text="USERNAME", font=("arial", 23))
user1.place(x=610, y=120)
user = Entry(width=17, bd=5, font=("arial", 20))
user.place(x=570, y=200)
label.pack(side=TOP, fill=X)
user2 = Label(text="PASSWORD", font=("arial", 23))
user2.place(x=610, y=280)
user3 = Entry(width=17, show="*", bd=5, font=("arial", 20))
user3.place(x=570, y=360)


def cat():
    firstw.destroy()
    print("hello everyone")

    import options
    options.options()
    """fn call me error tha, aur destroy method nahi chal rha, better destroy the frame yourself"""


def distroy():
    firstw.destroy()


def login():
    if user.get() == "1" and user3.get() == "1":
        print("running")
        cat()

    else:
        print("not working")
        t = tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ",
                                        "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
        user.delete(0, END)
        user3.delete(0, END)


button22 = Button(text="LOGIN", width=26, font=("arial", 10), bg="indianred1", command=login)
button22.place(x=600, y=481)
firstw.mainloop()
