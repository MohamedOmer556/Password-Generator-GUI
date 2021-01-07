from tkinter import *
from random import choice
import string
import pyperclip


root = Tk()
root.title('Password Generator by MOHA')
root.geometry('250x300')
root.resizable(0,0)   # fixed the height and width   - can't change them

head_line = Label(root, text='PASSWORD GENERATOR APP', font='arial 10 bold').place(x=30, y=10)
bottom_line = Label(root, text='Created by Moha', font='arial 10 bold').pack(side=BOTTOM)


pass_label = Label(root, text='PASSWORD LENGTH', font='arial 8 bold italic').place(x=70, y=40)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).place(x=80, y=65)


pass_str = StringVar()


def generator():
    password = ''
    for x in range(0, 4):
        password = choice(string.ascii_uppercase) + choice(string.ascii_lowercase) + choice(
            string.digits) + choice(string.punctuation)
    for y in range(pass_len.get() -4):
        password = password \
                   +choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    pass_str.set(password)


button = Button(root, text='Generate Password', command=generator).place(x=75, y=90)
input_text_field = Entry(root, textvariable=pass_str).place(x=75, y=120)


def copy_pass():
    pyperclip.copy(pass_str.get())


copy_button = Button(root, text='Copy Password', command=copy_pass).place(x=85, y=140)
root.mainloop()
