from tkinter import *
from tkinter import messagebox
from random import randint ,choice,shuffle
import pyperclip


def add():
    websitee = website_entry.get()
    usernamee = username_entry.get()
    passwordd = password_entry.get()
    if (len(websitee) > 0) and (len(usernamee) > 0) and (len(passwordd) > 0):
        save = messagebox.askokcancel(title = 'Save', message = f'Details entered\n Website:{websitee}\nEmail:{usernamee}\n Password:{passwordd}')
        with open('password_bank.txt', mode='a') as a:
            entries = a.write(f'{websitee} | {usernamee} | {passwordd}\n')
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


FONT_NAME = 'Courier'

window = Tk()
window.title('Password Manager')
window.config(padx = 50, pady = 50 , bg = 'white')

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

website_entry = Entry(width = 42)
website_entry.grid(column=1, row=1, columnspan = 2)
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

window.mainloop()