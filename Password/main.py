from tkinter import *
from tkinter import messagebox
from random import randint ,choice,shuffle
import pyperclip
import json


def add():
    websitee = website_entry.get()
    usernamee = username_entry.get()
    passwordd = password_entry.get()
    pass_dict = {
        websitee: {
            'email': usernamee,
            'password': passwordd

        }
    }

    if (len(websitee) > 0) and (len(usernamee) > 0) and (len(passwordd) > 0):
        try:
            with open('password_bank.json', mode='r') as pass_file:
                data = json.load(pass_file)
        except:
            with open('password_bank.json', mode='w') as pass_file:
                json.dump(pass_dict, pass_file, indent=4)

        else:
            with open('password_bank.json', mode='r') as pass_file:
                data.update(pass_dict)
                with open('password_bank.json', mode='w') as pass_file:
                    json.dump(data, pass_file, indent=4)

        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


    elif (len(websitee) == 0) or (len(usernamee) == 0) or (len(passwordd) == 0):
        messagebox.showerror(title='ERROR', message='Please fill all the fields')

def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pl = [choice(letters) for i in range(randint(8, 10))]
    ps = [choice(numbers) for j in range(randint(2, 4))]
    pn = [choice(symbols) for k in range(randint(2, 4))]

    password_list = pl + ps + pn
    shuffle(password_list)
    passwords = ''.join(password_list)
    password_entry.insert(0, passwords)
    pyperclip.copy(passwords)

def find_password():
    websitee = website_entry.get()
    try:
        with open('password_bank.json', 'r') as pass_file:
            data = json.load(pass_file)
    except:
        messagebox.showerror(title='Error', message='Details not found')

    else:
        if websitee in data:
            e = data[websitee]['email']
            p = data[websitee]['password']
            messagebox.showinfo(title=websitee, message=f'Email: {e}\nPassword: {p}')
        else:
            messagebox.showerror(title='Error', message='Details not found')



FONT_NAME = 'Courier'

window = Tk()
window.title('Password Manager')
window.config(padx = 30, pady = 30 , bg = 'white')

canvas = Canvas(width = 200, height = 200, bg = 'white', highlightthickness = 0)
img = PhotoImage(file = 'passimg.gif')
canvas.create_image(100,100,image = img)
canvas.grid(column =1,row = 0)

website = Label(text ='Website:',bg = 'white')
website.grid(column =0,row = 1,sticky='e')

username = Label(text ='Email/Username:',bg = 'white')
username.grid(column =0,row = 2,sticky='e')

passwordlabe = Label(text ='Password:', bg ='white')
passwordlabe.grid(column =0, row = 3, sticky='e')

website_entry = Entry(width = 23)
website_entry.grid(column=1, row=1)
website_entry.focus()
print(website_entry.get())

username_entry = Entry(width = 42)
username_entry.grid(column=1, row=2, columnspan = 2)
username_entry.insert(0,'haarishph71@gmail.com')
print(username_entry.get())

password_entry = Entry(width = 24)
print(password_entry.get())
password_entry.grid(column=1, row=3)

generate_button = Button(text = 'Generate Password', command=password_generation)
generate_button.grid(column = 2, row = 3, sticky='w')

add_button = Button(text = 'Add', width = 36, command=add)
add_button.grid(column = 1, row = 4, columnspan = 2)

search_button = Button(text = 'Search', width = 12, command= find_password)
search_button.grid(column = 2, row = 1)

window.mainloop()