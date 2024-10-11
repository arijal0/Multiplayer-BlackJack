# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *
import time

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

number_of_players = int(input("Welcome to Blackjack! How many players? "))


players = []
user_score = {}

for i in range(number_of_players):
    player_name = input(f"What is players {i+1}'s name? ")
    players.append(player_name)
    user_score[player_name] = 3


#Main Game Loop
gameOn = "y"
while gameOn == "y" and len(players) > 0:
  game_score = {}
  #Each Players Turn
  for player in players:
    user_hand = draw_starting_hand(player+"'S")
    should_hit = 'y'
    # player's coose to hit or stand
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

    #wait before switching player
    print("\n---Switching Player---")
    for i in range(3):
      print("...",end = "")
      time.sleep(0.5)
      
    print()
    

  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)

  # Determine results for each player
  print_header("GAME RESULT")
  for player, player_hand in game_score.items():
        
        if player_hand <= 21 and (player_hand > dealer_hand or dealer_hand > 21):
            user_score[player] += 1
            print(f"{player} wins! Score: {user_score[player]}")
        elif player_hand > 21 or (dealer_hand <= 21 and dealer_hand > player_hand):
            user_score[player] -= 1
            print(f"{player} loses! Score: {user_score[player]}")
        else:
            print(f"{player} pushes. Score: {user_score[player]}")

        # Eliminate player if their score is 0
        if user_score[player] == 0:
            print(f"{player} eliminated!")
            players.remove(player)
    
    # Check if all players are eliminated
  if len(players) == 0:
        print("All players eliminated!")
        break
    
    # Ask if they want to play another round
  gameOn = input("Do you want to play another hand (y/n)? ")
  if gameOn == "n":
        print("Game over!")