# Deck class will instantiate a new deck, shuffle a deck and deal cards from the deck
from Card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck():
  
  def __init__(self):
    self.all_cards = []

    for suit in suits:
      for rank in ranks:
        # Create the card object
        created_card = Card(suit, rank)
        self.all_cards.append(created_card)
  
  def shuffle(self):
    random.shuffle(self.all_cards)
  
  def deal_one(self):
    return self.all_cards.pop()

new_deck = Deck()

