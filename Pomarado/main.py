from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "COURIER"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text ='00:00')
    timer.config(text = 'TIMER', fg = GREEN)
    check.config(text ='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps ==3 or reps == 5 or reps == 7:
        timer.config(text = 'work', fg = GREEN)
        count_down(work_sec)
    if reps == 2 or reps ==4 or reps == 6:
        count_down(short_break_sec)
        timer.config(text = 'short break', fg = PINK)

    if reps == 8:
        count_down(long_break_sec)
        timer.config(text = 'long break',fg = RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds ='00'
    seconds = f"{seconds:02}"
    minutes = f"{minutes:02}"

    canvas.itemconfig(timer_text, text =f"{minutes} : {seconds}")
    if count > 0:
        global time
        time = window.after(1000,count_down, count -1)
    else:
        start_button()
        tick = ''
        session= math.floor(reps/2)
        for _ in range(session):
            tick += '✔'
            check.config(text = tick)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomarado')
window.config(padx = 180, pady = 80, bg = YELLOW)


canvas = Canvas(width = 200,height = 224, bg = YELLOW, highlightthickness = 0)
img = PhotoImage(file = 'tomato.png')
canvas.create_image(100,110,image = img)
timer_text = canvas.create_text(100,132,text ='00:00',fill = 'white', font=(FONT_NAME, 35,'bold'))
canvas.grid(column = 1, row = 1)

timer = Label(text ='TIMER', font =(FONT_NAME, 30, 'bold'),fg =GREEN, bg =YELLOW)
timer.grid(column = 1, row = 0)
timer.config(padx = 15,pady = 15)

check = Label(text ='', font =(FONT_NAME, 30, 'bold'),fg =GREEN, bg =YELLOW)
check.grid(column = 1, row = 3)
check.config(padx = 15,pady = 15)

start = Button(text = 'START', command = start_button,font=(FONT_NAME, 20), highlightthickness=0)
start.grid(column = 0, row = 2)

reset = Button(text = 'RESET', font=(FONT_NAME, 20), highlightthickness=0, command=reset)
reset.grid(column = 2, row = 2)

window.mainloop()