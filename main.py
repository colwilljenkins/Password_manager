from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pw_result.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pw_result.get()
    new_data = {website: {"email" : email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Missing details", message = "Oops you have left something empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent =4)
        else:
                #Updating old with new
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent = 4)
        finally:
            website_input.delete(0, END)
            pw_result.delete(0, END)

# --------------------FIND PASSWORD ------------------------------------#
def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email : {email}\nPassowrd: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {website} exists")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20, bg = 'white')

#setting up canvas and logo
canvas = Canvas(width = 200, height = 200, bg = 'white', highlightthickness = 0)
logo = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

#Labls of website, email and PASSWORD
web_label = Label(text = "Website", bg = 'white')
web_label.grid(row = 1, column = 0)

email_label = Label(text = "Email/Username:", bg = 'white')
email_label.grid(row = 2, column = 0)

pw_label = Label(text = "Password:", bg = 'white')
pw_label.grid(row = 3, column = 0)

#website and email entry boxes
website_input = Entry(width = 20)
website_input.grid(row = 1, column = 1, columnspan = 1)
website_input.focus()

email_input = Entry(width = 39)
email_input.grid(row = 2, column = 1, columnspan = 2, pady =5)
email_input.insert(0, "myemail@gmail.com")
#password box label
pw_result = Entry(width = 20)
pw_result.grid(row = 3, column = 1)

#generate and add buttons
gen_button = Button(text = "Generate Password", command = generate_password)
gen_button.grid(row = 3, column = 2)

add_button = Button(text ="Add", width = 34, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2, pady = 5)

# Search button
search_button = Button(text = "Search", width = 15, command = find_password)
search_button.grid(row = 1, column = 2, pady = 5)



window.mainloop()
