from pyperclip import copy
from tkinter import *
from tkinter import messagebox as msg
from random import choice, randint, shuffle


def gen_pass():
    """Function for password generation."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for j in range(randint(2, 4))]
    password_numbers = [choice(letters) for k in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0, password)
    copy(password)


def save():
    """Function that saves data to file."""
    web = entry_web.get()
    email = entry_email.get()
    passw = entry_pass.get()
    is_ok = msg.askokcancel(title=web, message=f"These are details:\nEmail: "
                                                   f"{email}\nPassword: {passw}\n"
                                                            f"Is it ok to save?")

    if len(web) == 0 or len(email) == 0 or len(passw) == 0:
        msg.showinfo(title="Error", message="Data fields cannot be empty!")
        is_ok = False

    if is_ok:
        f = open("data.txt", "a")
        f.write(web + " | " + email + " | " + passw + "\n")
        entry_web.delete(0, END)
        # entry_email.delete(0, END)
        entry_pass.delete(0, END)
        f.close()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label1 = Label(text="Website")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username")
label2.grid(row=2, column=0)
label3 = Label(text="Password")
label3.grid(row=3, column=0)

entry_web = Entry(width=35)
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "example@email.com")
entry_pass = Entry(width=18)
entry_pass.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", command=gen_pass)
gen_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
