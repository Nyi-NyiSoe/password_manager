from tkinter import *
import random

def frame(root,side):
    w = Frame(root)
    w.pack(side=side,expand=YES,fill=BOTH)
    return w

def button(root,side,text,command=None):
    w = Button(root,text=text,command=command)
    w.pack(side=side,expand=YES,fill=BOTH)

    return w

def create():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    sp_char = "@#$&_-()=%*:/!?+."

    str = lower + upper + numbers + sp_char
    length  = int(input("enter the length of your password! "))
    password = "".join(random.sample(str,8))
    return password

class psw_mnger(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Password Manager')

        display = StringVar()
        Entry(self,relief=SUNKEN,textvariable=display).grid(row=0,column=0)




if __name__ =='__main__':
    psw_mnger().mainloop()