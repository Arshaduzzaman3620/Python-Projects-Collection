from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Generated", message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showerror(title="Error ❌", message="Please fill out all fields.")
        return

    is_okay = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\n📧 Email: {email}\n🔑 Password: {password}\n\nSave?"
    )

    if is_okay:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        messagebox.showinfo(title="Saved ✅", message="Your credentials have been saved!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("🔐 Password Manager")
window.config(padx=40, pady=40, bg="#f7f7f7")

# Logo
canvas = Canvas(height=200, width=200, bg="#f7f7f7", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:", font=("Segoe UI", 10), bg="#f7f7f7").grid(row=1, column=0, sticky="e")
Label(text="Email/Username:", font=("Segoe UI", 10), bg="#f7f7f7").grid(row=2, column=0, sticky="e")
Label(text="Password:", font=("Segoe UI", 10), bg="#f7f7f7").grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, bg="#4CAF50", fg="white", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5)

add_button = Button(text="Add", width=36, bg="#2196F3", fg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=15)

window.mainloop()
