from tkinter import *

from streamlit import title


def button_op():
    value = input.get()
    v = float(value)
    fromu = selected_option.get()
    tou = selected_answer.get()

    conversion_factors = {
        "Miles": {"Miles": 1, "Km": 1.60934, "m": 1609.34, "cm": 160934, "mm": 1.609e+6},
        "Km": {"Miles": 0.621371, "Km": 1, "m": 1000, "cm": 100000, "mm": 1e+6},
        "m": {"Miles": 0.000621371, "Km": 0.001, "m": 1, "cm": 100, "mm": 1000},
        "cm": {"Miles": 6.2137e-6, "Km": 1e-5, "m": 0.01, "cm": 1, "mm": 10},
        "mm": {"Miles": 6.2137e-7, "Km": 1e-6, "m": 0.001, "cm": 0.1, "mm": 1},
    }

    if fromu in conversion_factors and tou in conversion_factors[fromu]:
        factor = conversion_factors[fromu][tou]
        answer = round(v*factor,12)
        value_l.config(text = answer)
    else:
        value_l.config(text = 'error')



window = Tk()
window.title('Units Converter')
window.minsize(1000,300)
window.config(padx = 10,pady = 10)

selected_option = StringVar()
selected_option.set("unit")  # Set the default value

options = ["Miles", "Km", "m", "cm", "mm"]

# Create the dropdown menu
dropdown_q = OptionMenu(window, selected_option, *options)
dropdown_q.config(width=10)  # Set width for consistency
dropdown_q.grid(column=0, row=0, padx=10, pady=10)


selected_answer = StringVar()
selected_answer.set("unit")  # Set the default value
# Create the dropdown menu
dropdown_a = OptionMenu(window, selected_answer, *options)
dropdown_a.config(width=10)  # Set width for consistency
dropdown_a.grid(column=4, row=0, padx=10, pady=10)

is_equal_to = Label(text = '=', font =('Comic Sans', 20))
is_equal_to.grid(column = 2, row = 0)
is_equal_to.config(padx = 15,pady = 15)

value_l = Label(text = 0, font =('Comic Sans', 15))
value_l.grid(column = 3, row = 0,sticky='e')
value_l.config(padx = 15,pady = 15)

input = Entry(width = 10,font=('Comic Sans', 15))
print(input.get())
input.grid(column=1, row=0,sticky='e')

calculate = Button(text = 'Calculate', command = button_op,font=('Comic Sans', 12))
calculate.grid(column = 2, row = 1)

window.mainloop()

