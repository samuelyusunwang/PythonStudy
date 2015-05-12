# Poker
from random import shuffle

class Card(object):
    """represents a standard playing cards."""
    
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: 
            return True
        elif self.suit > other.suit:
            return False
        elif self.rank < other.rank:
            return True
        else:
            return False
    def __gt__(self, other):
        return not self.__lt__(other)
    
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        shuffle(self.cards)
        
    def sort(self):
        self.cards.sort()
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        
    def deal_hands(self, num_hands, num_cards):
        hand_list = []
        for i in range(num_hands):
            hand = Hand()
            self.move_cards(hand, num_cards)
            hand_list.append(hand)
        return hand_list
        
        
# inheritance: Define the Hand class
class Hand(Deck):
    """represents a hand of playing cards"""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

        
        

# Test code
deck = Deck()
print(deck)

print('**********')
print('Shuffle the deck')
deck.shuffle()
print(deck)

print('**********')
print('Sort the deck')
deck.sort()
print(deck)

hand = Hand('new Hand')
print(hand.cards)
print(hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)

# Deal 5 hands of 5 cards
print('**********')
print('Deal 5 hands of 5')
deck.shuffle()
new_hands = deck.deal_hands(5, 5) 
for h in new_hands:
    print(h)








             