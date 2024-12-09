from tkinter import *

from streamlit import title

class Distance():
    def __init__(self):
        self.window = Tk()
        self.window.title('Units Converter')
        self.window.minsize(1000, 300)
        self.window.config(padx=10, pady=10)

        self.selected_option = StringVar()
        self.selected_option.set("unit")

        options = ["Miles", "Km", "m", "cm", "mm"]

        self.dropdown_q = OptionMenu(self.window, self.selected_option, *options)
        self.dropdown_q.config(width=10)  # Set width for consistency
        self.dropdown_q.grid(column=0, row=0, padx=10, pady=10)

        self.selected_answer = StringVar()
        self.selected_answer.set("unit")
        self.dropdown_a = OptionMenu(self.window, self.selected_answer, *options)
        self.dropdown_a.config(width=10)  # Set width for consistency
        self.dropdown_a.grid(column=4, row=0, padx=10, pady=10)

        self.is_equal_to = Label(text='=', font=('Comic Sans', 20))
        self.is_equal_to.grid(column=2, row=0)
        self.is_equal_to.config(padx=15, pady=15)

        self.value_l = Label(text=0, font=('Comic Sans', 15))
        self.value_l.grid(column=3, row=0, sticky='e')
        self.value_l.config(padx=15, pady=15)

        self.input = Entry(width=10, font=('Comic Sans', 15))
        print(self.input.get())
        self.input.grid(column=1, row=0, sticky='e')

        calculate = Button(text='Calculate', command=self.button_op, font=('Comic Sans', 12))
        calculate.grid(column=2, row=1)

        self.window.mainloop()

    def button_op(self):
        value = self.input.get()
        v = float(value)
        fromu = self.selected_option.get()
        tou = self.selected_answer.get()

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
            self.value_l.config(text = answer)
        else:
            self.value_l.config(text = 'error')





