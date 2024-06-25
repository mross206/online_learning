import random

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = [(suit, rank) for suit in suits for rank in ranks]
  random.shuffle(deck)
  return deck

def draw_card(deck, num_cards):
  hand = deck[:num_cards]
  del deck[:num_cards]
  return(hand, deck)

deck = create_deck()

def show_card(card):
  space = " "
  if len(card[1]) == 2:
    space = ""
  print (f"""
+-------+
|{card[1]}     {space}|
|       |
|   {card[0]}   |
|       |
|{space}     {card[1]}|
+-------+
""")

while len(deck) > 0:
  num_cards = int(input("How many cards do you want to draw?"))
  hand, deck = draw_card(deck, num_cards)
  for card in hand:
    show_card(card)

print("We are out of cards")