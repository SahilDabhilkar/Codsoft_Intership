import tkinter as tk

# Function to perform addition
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(f"Result: {num1 + num2}")
    except ValueError:
        result.set("Invalid input")

# Function to perform subtraction
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(f"Result: {num1 - num2}")
    except ValueError:
        result.set("Invalid input")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(f"Result: {num1 * num2}")
    except ValueError:
        result.set("Invalid input")

# Function to perform division
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            result.set("Result: Cannot divide by zero")
        else:
            result.set(f"Result: {num1 / num2}")
    except ValueError:
        result.set("Invalid input")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x500")

# Entry fields for input
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Buttons for operations
add_button = tk.Button(window, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(window, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(window, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(window, text="Divide", command=divide)
divide_button.pack()

# Result display
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Run the Tkinter main loop
window.mainloop()
