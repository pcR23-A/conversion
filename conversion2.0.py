import tkinter as tk
from tkinter import ttk

def convert():
    conversion = combo_box.get()
    value = float(entry.get())
    result = ""

    if conversion == 'Pounds to Kilograms':
        result = f"{round(value * 0.45, 2)} kg"
    elif conversion == 'Inches to Centimeters':
        result = f"{round(value * 2.54, 2)} cm"
    elif conversion == 'Feet to Metres':
        result = f"{round(value * 0.3, 2)} m"
    elif conversion == 'Kilograms to Pounds':
        result = f"{round(value * 2.2, 2)} lbs"
    elif conversion == 'Centimeters to Inches':
        result = f"{round(value * 0.39, 2)} in"
    elif conversion == 'Metres to Feet':
        result = f"{round(value * 3.28, 2)} ft"
    elif conversion == 'Kilometers to Miles':
        result = f"{round(value * 0.62, 2)} mi"
    elif conversion == 'Miles to Kilometers':
        result = f"{round(value * 1.61, 2)} km"
    elif conversion == 'Fahrenheit to Celsius':
        result = f"{round((value - 32) / 1.8, 2)} °C"
    elif conversion == 'Celsius to Fahrenheit':
        result = f"{round((value * 1.8) + 32, 2)} °F"
    elif conversion == 'Fluid Ounces to Millilitres':
        result = f"{round(value * 33.8, 2)} ml"
    elif conversion == 'Millilitres to Fluid Ounces':
        result = f"{round(value * 0.033, 2)} fl oz"
    else:
        result = "Invalid entry"

    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Measurement Converter")
root.resizable(False, False)
root.geometry("300x250")
# Create and place the widgets
label = ttk.Label(root, text="Choose a conversion:")
label.pack(pady=10)

combo_box = ttk.Combobox(root, values=[
    'Pounds to Kilograms',
    'Inches to Centimeters',
    'Feet to Metres',
    'Kilograms to Pounds',
    'Centimeters to Inches',
    'Metres to Feet',
    'Kilometers to Miles',
    'Miles to Kilometers',
    'Fahrenheit to Celsius',
    'Celsius to Fahrenheit',
    'Fluid Ounces to Millilitres',
    'Millilitres to Fluid Ounces'
])
combo_box.set('Pounds to Kilograms')
combo_box.pack(pady=5)

entry_label = ttk.Label(root, text="Enter the value:")
entry_label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=20)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
