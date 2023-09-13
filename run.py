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

# Function to clear console
def clear():
  if os.name == 'nt':
    os.system('CLS')
  if os.name == 'posix':
    os.system('clear')

# print results function
def print_results(dealer_hand, player_hand):
  clear()
  print("The dealer has a " + str(dealer_hand) + " for a total of " +
        str(total(dealer_hand)))
  print("You have a " + str(player_hand) + " for a total of " +
        str(total(player_hand)))

# Checking for blackjack
def blackjack(dealer_hand, player_hand):
  global wins
  global losses
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Congratulations! You got a Blackjack!\n")
    wins += 1
    print("losses", losses)
    print("wins", wins)
    play_again()
  elif total(dealer_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Sorry, you lose. The dealer got a blackjack.\n")
    losses += 1
    play_again()
    print("losses", losses)
    print("wins", wins)

# score options
def score(dealer_hand, player_hand):
  global wins
  global losses
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Congratulations! You got a Blackjack!\n")
    wins += 1
    print("losses", losses)
    print("wins", wins)
  elif total(dealer_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Sorry, you lose. The dealer got a blackjack.\n")
    losses += 1
    print("losses", losses)
    print("wins", wins)
  elif total(player_hand) > 21:
    print_results(dealer_hand, player_hand)
    print("Sorry. You busted. You lose.\n")
    losses += 1
    print("losses", losses)
    print("wins", wins)
  elif total(dealer_hand) > 21:
    print_results(dealer_hand, player_hand)
    print("Dealer busts. You win!\n")
    wins += 1
    print("losses", losses)
    print("wins", wins)
  elif total(player_hand) < total(dealer_hand):
    print_results(dealer_hand, player_hand)
    print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    losses += 1
    print("losses", losses)
    print("wins", wins)
  elif total(player_hand) > total(dealer_hand):
    print_results(dealer_hand, player_hand)
    print("Congratulations. Your score is higher than the dealer. You win\n")
    wins += 1
    print("losses", losses)
    print("wins", wins)

# combines functions
def game():
  global wins
  global losses
  clear()
  dealer_hand = deal(deck)
  player_hand = deal(deck)
  print("The dealer is showing a " + str(dealer_hand[0]))
  print("You have a " + str(player_hand) + " for a total of " +
        str(total(player_hand)))
  blackjack(dealer_hand, player_hand)
  while True:
    choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
    if choice == 'h':
        hit(player_hand)
        print(player_hand)
        print("Hand total: " + str(total(player_hand)))
        if total(player_hand) > 21:
            print('You busted')
            losses += 1
            print("losses", losses)
            print("wins", wins)
            play_again()
    elif choice == 's':
        while total(dealer_hand) <= 17:
            hit(dealer_hand)
            print(dealer_hand)
            if total(dealer_hand) > 21:
                print('Dealer busts, you win!')
                wins += 1
                print("losses", losses)
                print("wins", wins)
                play_again()
        score(dealer_hand, player_hand)
        play_again()
        exit()
    elif choice == 'q':
        exit()
    else:
        print("Invalid input. Please enter H, S, or Q.")