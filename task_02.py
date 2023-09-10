import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner and update the scores
def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    update_display(user_choice, computer_choice, result)

# Function to update the display
def update_display(user_choice, computer_choice, result):
    user_label.config(text=f"You chose {user_choice}")
    computer_label.config(text=f"Computer chose {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"User Score: {user_score}, Computer Score: {computer_score}")

# Function to handle user input
def user_choice_clicked(choice):
    determine_winner(choice)

# Create a Tkinter window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("500x500")

# Create labels and buttons
user_label = tk.Label(window, text="Choose an option:")
user_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: user_choice_clicked("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: user_choice_clicked("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: user_choice_clicked("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

computer_label = tk.Label(window, text="")
computer_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

score_label = tk.Label(window, text="")
score_label.pack()

# Start the Tkinter main loop
window.mainloop()
