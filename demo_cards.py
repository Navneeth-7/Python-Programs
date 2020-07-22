import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
matches = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
           'Jack': 10,
           'Queen': 10, 'King': 10, 'Ace': 11}
game_on = True
player_balance = 1000


class Card:
    # variable Decelaration
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    # Class Object Attribute
    deck = ['']

    def __init__(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        cards = '\nThis deck has the following cards: \n'
        for card in self.deck:
            cards += str(card.__str__() + "\n")
        return cards

    def suffle_deck(self):
        deck = random.shuffle(self.deck)
'''
    def deal_card(self):
        dealtcard = self.deck.pop()
        # print(len((Deck.deck)))
        return dealtcard
'''

deck = Deck()  # # Create new Deck instance.
deck.suffle_deck()  # Create & shuffle the deck, deal tw
print(deck)