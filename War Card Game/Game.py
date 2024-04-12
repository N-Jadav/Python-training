# Game setup
from Player import Player
from Deck import Deck

# Setup the Players
player_one = Player("One")
player_two = Player("Two")

# Setup the Deck
new_deck = Deck()
new_deck.shuffle()

# Deal the cards to players
for x in range (26):
  player_one.add_cards(new_deck.deal_one())
  player_two.add_cards(new_deck.deal_one())

# game_on to keep track if the game is still on
game_on = True
# round_num to keep track of what round
round_num = 0


while game_on:
  round_num += 1
  print(f"Round {round_num}")

  # Check if player one is out of cards
  if len(player_one.all_cards) == 0:
    print("Player One, out of cards! PLAYER TWO WINS!")
    game_on = False
    break

  # Check if player two is out of cards
  if len(player_two.all_cards) == 0:
    print("Player Two, out of cards! PLAYER ONE WINS!")
    game_on = False
    break

  # Start a new round
  # Both players will remove one cards from their hand and add it to show deck
  player_one_cards = []
  player_one_cards.append(player_one.remove_one())

  player_two_cards = []
  player_two_cards.append(player_two.remove_one())

  at_war = True

  while at_war:
    
    # Draw the last card, check who has the big card, that player gets all the cards
    if(player_one_cards[-1].value > player_two_cards[-1].value):

      player_one.add_cards(player_one_cards)
      player_one.add_cards(player_two_cards)
      at_war = False

    elif(player_one_cards[-1].value < player_two_cards[-1].value):

      player_two.add_cards(player_two_cards)
      player_two.add_cards(player_one_cards)
      at_war = False

    else:
      # War starts
      print('WAR!')

      if len(player_one.all_cards) < 5:
        print("Player One unable to declare war!")
        print("PLAYER TWO WINS!!")
        game_on = False
        break

      elif len(player_two.all_cards) < 5:
        print("Player Two unable to declare war!")
        print("PLAYER ONE WINS!!")
        game_on = False
        break

      else:
        for num in range(5):
          player_one_cards.append(player_one.remove_one())
          player_two_cards.append(player_two.remove_one())


      



