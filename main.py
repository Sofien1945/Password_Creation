"""Random Password Creation apps
Part of data flair training (Please visit: https://data-flair.training/blogs/python-password-generator/)
Date: 03.11.2021"""

# Import libraries
import tkinter.messagebox
import tkinter as tk
from tkinter import *
import random, string
import pyperclip

# Initialize main window
root = Tk()
root.geometry('400x200')
root.resizable(0, 0)
root.title("PASSWORD GENERATOR (Beta.0)")

# Write Information labels on the window
Label(root, text='Password Generator', font='calibri 15 bold').pack(side=TOP)
Label(root, text='Version Beta.0', font='tahoma 13 bold').pack(side=BOTTOM)

# Write Password labels on the window
pass_label = Label(root, text='Password Length', font='arial 10 bold').pack(side=LEFT)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack(side=LEFT)
pass_str = StringVar()


# Crate the password generation function
def Generator():
    password = ''
    # for x in range(0,4):
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
        string.digits) + random.choice(string.punctuation)

    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_str.set(password)


# Create password generator button
Button(root, text="Click for Pass Generation: ", command=Generator).pack(pady=10)
Entry(root, textvariable=pass_str).pack()


# Password copy function + Button
def Copy_password():
    pyperclip.copy(pass_str.get())
    tkinter.messagebox.showinfo(title="Information", message="Copied to clipboard")


Button(root, text="Copy to clipboard", command=Copy_password).pack(pady=10)

root.mainloop()

