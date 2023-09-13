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
        print("goodbye")
        exit()
    else:
        print("Invalid input. Please enter H, S, or Q.")


#----------------------------------- computer 


# Asking which mode user wants
while True:
  PvC= input("Do you want to play PvC? (Y/N) : ").lower()
  if PvC == 'y' or PvC == 'n':
      break
  else:
     print('Invalid input. Please enter Y or N.')

if PvC == 'y':
    dealer_hand = []
    player_hand = []
    game()
elif PvC == 'n':
    while True:
        CvC = input("Do you want to play CvC? (Y/N): ").lower()
        if CvC == 'y' or CvC == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    if CvC == 'y':
        num_games = int(input("How many games would you like to play? "))
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    elif CvC == 'n':
        print('Okay goodbye')
        exit()
    else:
        print('Invalid input. Please enter Y or N.')

# Function for computer to play game
def play_game(num_decks=1):
    deck = card_values * 4 * num_decks  
    random.shuffle(deck)  
    player_hand = [deck.pop(), deck.pop()]  
    dealer_hand = [deck.pop(), deck.pop()]  

    
    while sum_card_values(player_hand) < 18:
        player_hand.append(deck.pop())

    
    while sum_card_values(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    player_total = sum_card_values(player_hand)  
    dealer_total = sum_card_values(dealer_hand)  


    if player_total > 21:
        result = 'Dealer wins'
    elif dealer_total > 21:
        result = 'Player wins'
    elif player_total > dealer_total:
        result = 'Player wins'
    elif dealer_total > player_total:
        result = 'Dealer wins'
    else:
        result = 'draw'

    return result  

# calculate value of cards
def sum_card_values(hand):
      sum = 0
      num_aces = 0
      for value in hand:
          if value == 'A':
              num_aces += 1
          elif value in ['K', 'Q', 'J']:
              sum += 10
          else:
              sum += int(value)
      for _ in range(num_aces):
          if sum + 11 > 21:
              sum += 1
          else:
              sum += 11
      return sum

# Playing the game for number of times that is stated 
player_wins = dealer_wins = draws = player_losses = dealer_losses = draws = 0

for i in range(num_games):
    result = play_game()
    if result == 'Player wins':
        player_wins += 1
        dealer_losses += 1
    elif result == 'Dealer wins':
        dealer_wins += 1
        player_losses += 1
    elif result == 'draw':
        draws += 1

#display game results
print(f'Player wins: {player_wins}')
print(f'Player losses: {player_losses}')
print(f'Dealer wins: {dealer_wins}')
print(f'Dealer losses: {dealer_losses}')
print(f'draws: {draws}')

new_file = 'new.csv'
new_data = [("players wins", player_wins),("player losses", player_losses), ("dealer wins", dealer_wins),("dealer losses", dealer_losses),("draws", draws)]

# read results
with open(new_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i+1, player_wins, player_losses, dealer_wins, dealer_losses,draws])
with open(new_file, 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

data.pop(0)

# take data from csv
player_wins = [int(row[1]) for row in data]
player_losses = [int(row[2]) for row in data]
dealer_wins = [int(row[3]) for row in data]
dealer_losses = [int(row[4]) for row in data]
draws = []
for row in data:
    if len(row) >= 6:
        draws.append(int(row[5]))

# display data using pie and bar chart
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
barlabels = ['Player Wins', 'Player Losses', 'Dealer Wins', 'Dealer Losses']
barvalues = [sum(player_wins), sum(player_losses), sum(dealer_wins), sum(dealer_losses)]
ax1.bar(barlabels, barvalues)
ax1.set_title('Total Results')
x = [row[0] for row in data]
y = [int(row[1]) - int(row[2]) for row in data] 
total_games = sum(barvalues) + sum(draws)
player_win_pct = sum(player_wins) / total_games * 100
player_loss_pct = sum(player_losses) / total_games * 100
dealer_win_pct = sum(dealer_wins) / total_games * 100
dealer_loss_pct = sum(dealer_losses) / total_games * 100
draw_pct = sum(draws) / total_games * 100
labels = ['Player Wins', 'Player Losses', 'Dealer Wins', 'Dealer Losses', 'Draws']
sizes = [player_win_pct, player_loss_pct, dealer_win_pct, dealer_loss_pct, draw_pct]
colors = ['green', 'red', 'blue', 'orange', 'gray']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')
ax2.set_title('Game Outcomes')

#show plot points 
plt.show()