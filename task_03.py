import random
import string
import tkinter as tk
import pyperclip

def generate_password(length, complexity, exclude_lower, exclude_upper, exclude_digits, exclude_symbols):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?/\\"
    
    # Exclude selected character sets
    excluded_sets = 0
    pool = ""
    if not exclude_lower:
        pool += lower_case
    else:
        excluded_sets += 1
    if not exclude_upper:
        pool += upper_case
    else:
        excluded_sets += 1
    if not exclude_digits:
        pool += digits
    else:
        excluded_sets += 1
    if not exclude_symbols:
        pool += special_chars
    else:
        excluded_sets += 1
    
    if excluded_sets > 3:
        raise ValueError("Cannot exclude more than 3 character sets.")
    
    # Generate the password
    password = ''.join(random.choice(pool) for _ in range(length))
    
    return password

def generate_password_button():
    try:
        length = int(length_scale.get())
        complexity = int(complexity_scale.get())
        exclude_lower = exclude_lower_var.get()
        exclude_upper = exclude_upper_var.get()
        exclude_digits = exclude_digits_var.get()
        exclude_symbols = exclude_symbols_var.get()
        
        if length <= 0:
            result_label.config(text="Length should be a positive integer.")
        else:
            password = generate_password(length, complexity, exclude_lower, exclude_upper, exclude_digits, exclude_symbols)
            result_label.config(text="Generated Password: " + password)
            generated_password.set(password)  # Set the password to a tkinter StringVar
    except ValueError as e:
        result_label.config(text=str(e))

def copy_password_button():
    password_to_copy = generated_password.get()
    if password_to_copy:
        pyperclip.copy(password_to_copy)
        result_label.config(text="Password Copied to Clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and arrange widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_scale = tk.Scale(root, from_=1, to=128, orient="horizontal", label="Length (1-128)")
length_scale.pack()

complexity_label = tk.Label(root, text="Complexity Level:")
complexity_label.pack()
complexity_scale = tk.Scale(root, from_=1, to=4, orient="horizontal", label="1: Lowercase, 2: Uppercase, 3: Digits, 4: Special Characters")
complexity_scale.pack()

exclude_frame = tk.Frame(root)
exclude_frame.pack()

exclude_lower_var = tk.BooleanVar()
exclude_upper_var = tk.BooleanVar()
exclude_digits_var = tk.BooleanVar()
exclude_symbols_var = tk.BooleanVar()

exclude_lower_check = tk.Checkbutton(exclude_frame, text="Exclude Lowercase", variable=exclude_lower_var)
exclude_upper_check = tk.Checkbutton(exclude_frame, text="Exclude Uppercase", variable=exclude_upper_var)
exclude_digits_check = tk.Checkbutton(exclude_frame, text="Exclude Digits", variable=exclude_digits_var)
exclude_symbols_check = tk.Checkbutton(exclude_frame, text="Exclude Symbols", variable=exclude_symbols_var)

exclude_lower_check.pack(side="left")
exclude_upper_check.pack(side="left")
exclude_digits_check.pack(side="left")
exclude_symbols_check.pack(side="left")

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button)
generate_button.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password_button)
copy_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# StringVar to store the generated password
generated_password = tk.StringVar()

# Start the Tkinter main loop
root.mainloop()
