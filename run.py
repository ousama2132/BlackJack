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

def deal(deck):
  hand = []
  for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
  return hand

# Play again function
def play_again():
  again = input("Do you want to play again? (Y/N) : ").lower()
  if again == "y":
    dealer_hand = []
    player_hand = []
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    game()
  elif again == "n":
    print("Bye")
    exit()    
  else:
    print("invalid input")

# calculates A card
def total(hand):
  total = 0
  for card in hand:
    if card == "J" or card == "Q" or card == "K":
      total += 10
    elif card == "A":
      if total >= 11: total += 1
      else: total += 11
    else: total += card
  return total

# Function to hit
def hit(hand):
  card = deck.pop()
  if card == 11: card = "J"
  if card == 12: card = "Q"
  if card == 13: card = "K"
  if card == 14: card = "A"
  hand.append(card)
  return hand