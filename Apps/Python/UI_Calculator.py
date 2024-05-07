import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function to update the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
