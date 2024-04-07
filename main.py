import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from string import ascii_letters, digits, punctuation


def password_generator():
    password_ent.delete(0, END)

    letters = list(ascii_letters)
    numbers = list(digits)
    symbols = list(punctuation)

    letters_lst = [choice(letters) for _ in range(randint(8, 10))]
    numbers_lst = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_lst = [choice(symbols) for _ in range(randint(2, 4))]

    password = letters_lst + numbers_lst + symbols_lst
    shuffle(password)
    password = "".join(password)

    password_ent.insert(0, password)
    pyperclip.copy(password)  # copy to clipboard


def add_info():
    website = website_ent.get()
    email = email_ent.get()
    password = password_ent.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You've left a field empty.")
    else:
        user_check = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n Email: {email}\n Password: {password}\n\n Is it OK to save?")

        if user_check:
            website_ent.delete(0, END)
            website_ent.focus()
            password_ent.delete(0, END)

            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")


root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)

email_lb = Label(text="Email/Username:")
email_lb.grid(row=2, column=0)

password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

# entries
website_ent = Entry()
website_ent.grid(row=1, column=1, columnspan=2, sticky=EW)
website_ent.focus()

email_ent = Entry()
email_ent.grid(row=2, column=1, columnspan=2, sticky=EW)
email_ent.insert(0, "test@gmail.com")

password_ent = Entry()
password_ent.grid(row=3, column=1, sticky=EW)

# buttons
generate_btn = Button(text="Generate Password", command=password_generator)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", command=add_info)
add_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

root.mainloop()
