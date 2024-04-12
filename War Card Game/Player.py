# Player class will hold a player's list of cards, player should be able to add, remove cards from their hand(list of cards)
class Player:

  def __init__(self, name) -> None:
    self.name = name
    self.all_cards = []
  
  def remove_one(self):
    return self.all_cards.pop(0)
  
  def add_cards(self, new_cards):

    if type(new_cards) == type ([]):
      # To all multiple cards
      self.all_cards.extend(new_cards)
    else:
      # To add single card
      self.all_cards.append(new_cards)
  
  def __str__(self) -> str:
    return f'Player {self.name} has {len(self.all_cards)} cards'
    

