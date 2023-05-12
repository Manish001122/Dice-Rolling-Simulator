import tkinter as tk
import random

# Function to simulate rolling a pair of dice
def roll_dice():
    # Generate random numbers between 1 and 6 for each die
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    # Update the label text with the dice values
    result_label.config(text="Dice 1: {}   Dice 2: {}".format(dice1, dice2))

# Create the main window
window = tk.Tk()
window.title("Dice Rolling Simulator")

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Create a button to roll the dice
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

# Start the main event loop
window.mainloop()
