dist_options = ["Miles", "Km", "m", "cm", "mm"]

dist_conversion_factors = {
            "Miles": {"Miles": 1, "Km": 1.60934, "m": 1609.34, "cm": 160934, "mm": 1.609e+6},
            "Km": {"Miles": 0.621371, "Km": 1, "m": 1000, "cm": 100000, "mm": 1e+6},
            "m": {"Miles": 0.000621371, "Km": 0.001, "m": 1, "cm": 100, "mm": 1000},
            "cm": {"Miles": 6.2137e-6, "Km": 1e-5, "m": 0.01, "cm": 1, "mm": 10},
            "mm": {"Miles": 6.2137e-7, "Km": 1e-6, "m": 0.001, "cm": 0.1, "mm": 1},
        }

mass_options = ["Kilograms", "Pounds", "Grams", "Ounces", "Milligrams"]

mass_conversion_factors = {
    "Kilograms": {
        "Kilograms": 1,
        "Pounds": 2.20462,
        "Grams": 1000,
        "Ounces": 35.274,
        "Milligrams": 1e+6
    },
    "Pounds": {
        "Kilograms": 0.453592,
        "Pounds": 1,
        "Grams": 453.592,
        "Ounces": 16,
        "Milligrams": 453592
    },
    "Grams": {
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Grams": 1,
        "Ounces": 0.035274,
        "Milligrams": 1000
    },
    "Ounces": {
        "Kilograms": 0.0283495,
        "Pounds": 0.0625,
        "Grams": 28.3495,
        "Ounces": 1,
        "Milligrams": 28349.5
    },
    "Milligrams": {
        "Kilograms": 1e-6,
        "Pounds": 2.2046e-6,
        "Grams": 0.001,
        "Ounces": 3.5274e-5,
        "Milligrams": 1
    },
}

vol_options = ["Liters", "Milliliters", "Cubic Meters", "Gallons", "Cups"]

vol_conversion_factors = {
    "Liters": {
        "Liters": 1,
        "Milliliters": 1000,
        "Cubic Meters": 0.001,
        "Gallons": 0.264172,
        "Cups": 4.22675
    },
    "Milliliters": {
        "Liters": 0.001,
        "Milliliters": 1,
        "Cubic Meters": 1e-6,
        "Gallons": 0.000264172,
        "Cups": 0.00422675
    },
    "Cubic Meters": {
        "Liters": 1000,
        "Milliliters": 1e+6,
        "Cubic Meters": 1,
        "Gallons": 264.172,
        "Cups": 4226.75
    },
    "Gallons": {
        "Liters": 3.78541,
        "Milliliters": 3785.41,
        "Cubic Meters": 0.00378541,
        "Gallons": 1,
        "Cups": 16
    },
    "Cups": {
        "Liters": 0.236588,
        "Milliliters": 236.588,
        "Cubic Meters": 0.000236588,
        "Gallons": 0.0625,
        "Cups": 1
    },
}

temp_options = ["Celsius", "Fahrenheit", "Kelvin"]

temp_conversion_factors = {
    "Celsius": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    },
    "Fahrenheit": {
        "Celsius": lambda x: (x - 32) * 5/9,
        "Fahrenheit": lambda x: x,
        "Kelvin": lambda x: (x - 32) * 5/9 + 273.15
    },
    "Kelvin": {
        "Celsius": lambda x: x - 273.15,
        "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32,
        "Kelvin": lambda x: x
    },
}

