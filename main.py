import json
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
    data_dict = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Website or password field is empty.")
    else:
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open("data.json", "w") as json_file:
                json.dump(data_dict, json_file, indent=4)
        else:
            data.update(data_dict)
            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
        finally:
            website_ent.delete(0, END)
            website_ent.focus()
            password_ent.delete(0, END)


def search_data():
    website = website_ent.get()

    if len(website) > 0:
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="File data not found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"\nEmail: {email} \nPassword: {password} \n\nPassword copied to clipboard")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Oops", message=f"{website} was not found in data file.")
    else:
        messagebox.showinfo(title="Oops", message="Enter a website name to search.")


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
website_ent.grid(row=1, column=1, sticky=EW)
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

search_btn = Button(text="Search", command=search_data)
search_btn.grid(row=1, column=2, sticky=EW)

root.mainloop()
