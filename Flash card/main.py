from tkinter import *
import pandas as pd
from random import randint, choice

window = Tk()
window.title('Flash Card')
window.config(padx = 50, pady = 50,bg = 'white')

canvas = Canvas(width = 397, height = 421, highlightthickness = 0,bg='white')
cf = PhotoImage(file = 'chorts.png')
canvas.create_image(198,190,image = cf)
canvas.create_text(200,120, text = 'Title',font = ('Segoe Print', 20, 'normal'))
canvas.create_text(200,180, text = 'question',font = ('Segoe Print', 20, 'bold'))
canvas.grid(column = 0,row = 0, columnspan = 2)

canvas = Canvas(width = 100, height = 100, highlightthickness = 0,bg='white')
r = PhotoImage(file = 'true.png')
canvas.create_image(50,50,image = r)
right = Button(window,image = r, highlightthickness = 0,bd = 0,relief = FLAT)
right.grid(column = 0, row = 1)

canvas = Canvas(width = 100, height = 99, highlightthickness = 0,bg='white')
w = PhotoImage(file = 'false.png')
canvas.create_image(50,50,image = w)
wrong = Button(window,image = w,bd = 0, highlightthickness = 0, relief = FLAT)
wrong.grid(column = 1, row = 1)

d = pd.read_csv('ds_Flash_card.csv')
df = pd.DataFrame(d)
dict = {row['Concept']:row['Description'] for _,row in df.iterrows()}







window.mainloop()


