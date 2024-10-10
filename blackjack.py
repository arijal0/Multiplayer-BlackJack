# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *
import time

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

number_of_players = int(input("Welcome to Blackjack! How many players? "))
players = []
for i in range(number_of_players):
  users = input(f"What is players {i+1}'s name? ")
  players.append(users)

user_score = {}
for player in players:
  user_score[player] = 3

game_score = {}
for player in players:
  user_hand = draw_starting_hand(player+"'S")
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
  game_score[player] = user_hand
  print_end_turn_status(user_hand)


  print("\n---Switching Player---")
  for i in range(5):
    print("...",end = "")
    time.sleep(0.5)
    
  print()
  

# DEALER'S TURN
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  dealer_hand = dealer_hand + draw_card()
game_score["DEALER"] = dealer_hand
print_end_turn_status(dealer_hand)




# GAME RESULT
print_end_game_status(user_hand, dealer_hand)