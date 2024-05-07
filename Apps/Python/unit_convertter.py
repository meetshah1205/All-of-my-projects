import tkinter as tk

def convert():
    conversion_number, from_unit, to_unit = conversions_available.get(conversion_var.get())
    from_value = float(entry_from_value.get())
    to_value = None

    if conversion_number == 1:
        to_value = from_value * 0.621371
    elif conversion_number == 2:
        to_value = from_value * 1.61
    elif conversion_number == 3:
        to_value = from_value * 2.20462
    elif conversion_number == 4:
        to_value = from_value * 0.453592
    elif conversion_number == 5:
        to_value = (from_value - 32) / 1.8
    elif conversion_number == 6:
        to_value = from_value * 1.8 + 32

    result_label.config(text=f'{from_value} {from_unit} --> {to_value} {to_unit}')

# Create a Tkinter window
window = tk.Tk()
window.title('Unit Converter')

# Define conversion options
conversions_available = {
    '1': (1, 'km', 'mi'),
    '2': (2, 'mi', 'km'),
    '3': (3, 'kg', 'lbs'),
    '4': (4, 'lbs', 'kg'),
    '5': (5, '°F', '°C'),
    '6': (6, '°C', '°F'),
}

# Create labels and entry fields
conversion_label = tk.Label(window, text='Select Conversion:')
conversion_label.pack()
conversion_var = tk.StringVar()
conversion_var.set('1')  # Default to the first conversion
conversion_dropdown = tk.OptionMenu(window, conversion_var, *conversions_available.keys())
conversion_dropdown.pack()

from_label = tk.Label(window, text='Enter Value:')
from_label.pack()
entry_from_value = tk.Entry(window)
entry_from_value.pack()

convert_button = tk.Button(window, text='Convert', command=convert)
convert_button.pack()

result_label = tk.Label(window, text='')
result_label.pack()

window.mainloop()

