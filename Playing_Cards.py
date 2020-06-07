import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#ranks={'Ace','Two'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
           'Jack': 10,
           'Queen': 10, 'King': 10, 'Ace': 11}
playing  = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank+ " of "+self.suit

class Deck:

    def __init__(self):
        self.deck = ['']
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self):
        cards = '\nThis deck has the following cards: \n'
        for card in self.deck:
            cards +=str(card.__str__() + "\n")
        return "The Deck has "+cards


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealtcard = self.deck.pop()
        # print(len((Deck.deck)))
        return dealtcard

class Hand:
    def __init__(self):
        self.cards = []
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+= values[card.rank]

        if card.rank == 'Ace':
            self.aces+=1
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1

'''
test_deck=Deck()
test_deck.shuffle()
#Player
test_player=Hand()
pulled_card= test_deck.deal()
print(f"  {pulled_card}")
test_player.add_card(pulled_card)
print(test_player.value)
while True:
    pulled_card= test_deck.deal()
    print(f"  {pulled_card}")
    test_player.add_card(pulled_card)
    print(test_player.value)
'''

class Chips:
    def __init__(self,total=100):
        self.total= total
        self.bet= 0
    def win_bet(self):
        self.total+=self.bet
    def loose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips you want to bet:"))
        except:
            print("OOps! not and interger")
        else:
            if  chips.bet>chips.total:
                print(f"Insufficent chips, you have {chips.total}")
            else:
                break

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    playing = True
    while True:
        x=input("Hit or Stand? Enter h or s: ")
        if x[0].lower() == 'h':
            hit(deck,hand)
            return True
        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn ")
            return False
        else:
            print("Please Enter h or s")
            continue
        break

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.loose_bet()
def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('Player Wins! Dealer Bust!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.loose_bet()
def push(player,dealer):
    print("Dealer and player Tie!")

def show_some(player,dealer):
    print("Dealer Hand:")
    print("One card Hidden!")
    print(dealer.cards[1])
    print("\n")
    print("Players Hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("Dealers Hand!:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player Hand!:")
    for card in player.cards:
        print(card)

#logic

while True:
    print("Welcome to Black Jack")
    deck=Deck()
    deck.shuffle()
    player_hand= Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
    while playing:
        playing = hit_or_stand(deck,player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # IF player < 21
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value >player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print("\n Player Total Chips are : ".format(player_chips.total))
    new_game=input("Do you want to play? y or n:")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("THank you for playing!")
        break





