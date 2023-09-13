# ASCII Art
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# Import required modules
import os
import random
import csv
import matplotlib.pyplot as plt

# Print the game logo
print(logo)

# Take input for the number of decks to use in the game
while True:
    decks_input = input("Enter number of decks: ")
    try:
        decks = int(decks_input)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Define a deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 


wins = 0
losses = 0
wins2 = 0
losses2 = 0