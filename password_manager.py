from tkinter import *
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
sp_char = "@#$&_-()=%*:/!?+."

str = lower + upper + numbers + sp_char
length  = int(input("enter the length of your password! "))
password = "".join(random.sample(str,8))
print( password)