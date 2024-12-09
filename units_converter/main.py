from tkinter import *
from distance import Distance

# Create an instance of Distance
dist_obj = Distance()

# Initialize window
window = Tk()
window.title("Units Converter")
window.minsize(1000, 300)
window.config(padx=10, pady=10)

# Variables for options and factors
options = []
conversion_factors = {}

# Function to handle radio button selection and update options
def select_conversion():
    selected_value = conversion.get()
    global options, conversion_factors

    if selected_value == "Distance":
        options = dist_obj.dist_options
        conversion_factors = dist_obj.dist_conversion_factors
    elif selected_value == "Weight/Mass":
        options = dist_obj.mass_options
        conversion_factors = dist_obj.mass_conversion_factors
    elif selected_value == "Volume":
        options = dist_obj.vol_options
        conversion_factors = dist_obj.vol_conversion_factors
    elif selected_value == "Temperature":
        options = dist_obj.temp_options
        conversion_factors = dist_obj.temp_conversion_factors

    # Update dropdowns
    update_dropdowns()

    result_label.config(text=f"You selected: {selected_value}")

# Function to update dropdown menus dynamically
def update_dropdowns():
    dropdown_q["menu"].delete(0, "end")
    dropdown_a["menu"].delete(0, "end")
    for option in options:
        dropdown_q["menu"].add_command(label=option, command=lambda opt=option: selected_option.set(opt))
        dropdown_a["menu"].add_command(label=option, command=lambda opt=option: selected_answer.set(opt))

# Function for calculation
def calculate_conversion():
    value = input.get()
    try:
        v = float(value)
        from_unit = selected_option.get()
        to_unit = selected_answer.get()

        if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
            if callable(conversion_factors[from_unit][to_unit]):  # For temperature conversions
                answer = conversion_factors[from_unit][to_unit](v)
            else:  # For other conversions
                answer = v * conversion_factors[from_unit][to_unit]
            value_l.config(text=round(answer, 4))
        else:
            value_l.config(text="Error")
    except ValueError:
        value_l.config(text="Invalid Input")

# Radio buttons for category selection
conversion = StringVar()
conversion.set(" ")

radio1 = Radiobutton(window, text="Distance", variable=conversion, value="Distance", command=select_conversion)
radio2 = Radiobutton(window, text="Weight/Mass", variable=conversion, value="Weight/Mass", command=select_conversion)
radio3 = Radiobutton(window, text="Volume", variable=conversion, value="Volume", command=select_conversion)
radio4 = Radiobutton(window, text="Temperature", variable=conversion, value="Temperature", command=select_conversion)

radio1.pack(anchor=W, padx=10, pady=5)
radio2.pack(anchor=W, padx=10, pady=5)
radio3.pack(anchor=W, padx=10, pady=5)
radio4.pack(anchor=W, padx=10, pady=5)

result_label = Label(window, text="You selected: ", font=("Arial", 12))
result_label.pack(pady=10)

# Dropdowns for unit selection
selected_option = StringVar()
selected_option.set("unit")

dropdown_q = OptionMenu(window, selected_option, "")
dropdown_q.config(width=10)
dropdown_q.grid(column=0, row=0, padx=10, pady=10)

selected_answer = StringVar()
selected_answer.set("unit")

dropdown_a = OptionMenu(window, selected_answer, "")
dropdown_a.config(width=10)
dropdown_a.grid(column=4, row=0, padx=10, pady=10)

# Labels and input field
is_equal_to = Label(text="=", font=("Comic Sans", 20))
is_equal_to.grid(column=2, row=0)
is_equal_to.config(padx=15, pady=15)

value_l = Label(text="0", font=("Comic Sans", 15))
value_l.grid(column=3, row=0, sticky="e")
value_l.config(padx=15, pady=15)

input = Entry(width=10, font=("Comic Sans", 15))
input.grid(column=1, row=0, sticky="e")

# Calculate button
calculate_button = Button(text="Calculate", command=calculate_conversion, font=("Comic Sans", 12))
calculate_button.grid(column=2, row=1)

window.mainloop()
