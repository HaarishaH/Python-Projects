from tkinter import *
import pandas as pd
from random import randint, choice
import textwrap

current_card = {}
cards= {}
window = Tk()
window.title('Flash Card')
window.config(padx = 50, pady = 50,bg = 'white')

try:
    df = pd.read_csv('unknown_words.csv')
except:
    original = pd.read_csv('ds_Flash_card.csv')
    cards = original.to_dict(orient='records')
else:
    cards = df.to_dict(orient = 'records')
print(cards)

def next():
    global current_card,flip
    window.after_cancel(flip)
    current_card = choice(cards)
    wrapped_text = textwrap.fill(current_card['Description'], width=20)
    canvas.itemconfig(card_description,text = 'Description')
    canvas.itemconfig(card_sentence, text=wrapped_text)
    flip = window.after(3000,func = flipped)

def flipped():
    global current_card
    wrapped_text_c = textwrap.fill(current_card['Concept'], width=20)
    canvas.itemconfig(card_description, text='Concept')
    canvas.itemconfig(card_sentence, text=wrapped_text_c)

def known():
    cards.remove(current_card)
    print(len(cards))
    df= pd.DataFrame(cards)
    df.to_csv('unknown_words.csv')
    next()

flip = window.after(3000,func = flipped)

canvas = Canvas(width = 397, height = 421, highlightthickness = 0,bg='white')
cf = PhotoImage(file = 'chorts.png')
canvas.create_image(198,190,image = cf)
card_description = canvas.create_text(200,90, text = '',font = ('Segoe Print', 20, 'bold'))
card_sentence = canvas.create_text(200,200, text = '',font = ('Segoe Print', 15, 'normal'))
canvas.grid(column = 0,row = 0, columnspan = 2)

r = PhotoImage(file = 'true.png')
right = Button(window,image = r, highlightthickness = 0,bd = 0,relief = FLAT, command=known)
right.grid(column = 1, row = 1)

w = PhotoImage(file = 'false.png')
wrong = Button(window,image = w,bd = 0, highlightthickness = 0, relief = FLAT,command=next)
wrong.grid(column = 0, row = 1)



next()





window.mainloop()


