import string
from tkinter import *
import random
import pyperclip


def generator():
    # Get the password length from the Spinbox
    password_length = int(length_Box.get())

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters

    # Use random.sample() to generate a random password
    password = random.sample(all_characters, password_length)

    if choice.get() == 1:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(small_alphabets, password_length)))
    elif choice.get() == 2:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(small_alphabets + capital_alphabets, password_length)))
    elif choice.get() == 3:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(all_characters, password_length)))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg="cyan")
choice = IntVar()
Font = ('arial', 13, 'bold')

passwordlabel = Label(root, text="Password Generator", font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordlabel.grid()

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice)
weakradioButton.grid(pady=10)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice)
mediumradioButton.grid(pady=10)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice)
strongradioButton.grid(pady=10)

lengthlabel = Label(root, text="Password length", font=Font, bg='gray20', fg='white')
lengthlabel.grid()

length_Box = Spinbox(root, from_=1, to=12, width=5, font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate Password', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()
