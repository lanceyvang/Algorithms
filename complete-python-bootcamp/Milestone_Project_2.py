import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += f'\n{card.__str__()}'
        return f'The deck has: {deck_comp}'
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input(f'How many chips would you like to bet? you have {chips.total} chips: '))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total}')
            else:
                break

def hit(deck,hand):
    '''
    Write a function for taking hits
    '''
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    for card in hand.cards:
        print(card)
    print(f'TOTAL: {hand.value}')

def hit_or_stand(deck, hand):
    '''
    Write a function prompting the Player to Hit or Stand
    '''
    
    go = True

    while go and hand.value < 21:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            go = False

        else:
            print('Sorry, I did not understand that, Please enter h or s only!')
            continue
        
        # break

# Write functions to display cards
def show_some(player, dealer):
    print(f'DEALERS HAND: ???')
    print('ONE CARD HIDDEN!')
    print(dealer.cards[1])
    print('\n')
    print(f'PLAYERS HAND: {player.value}')
    for card in player.cards:
        print(card)
    print('------')

def show_all(player, dealer):
    print(f'DEALERS HAND: {dealer.value}')
    for card in dealer.cards:
        print(card)
    print('\n')
    print(f'PLAYERS HAND: {player.value}')
    for card in player.cards:
        print(card)
    print('---RESULTS---')


def player_busts(player, dealer, chips):
    print('Player BUST! Dealer Wins!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print(f'Player Wins! {player.value} to {dealer.value}')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer BUST! Player wins!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print(f'Dealer Wins! {dealer.value} to {player.value}')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Dealer and player tie! PUSH')

# GAME
while True:

    # Print and opening statement.
    print('Welcome to BlackJack')
    # Create & shuffle the deak, deal two cards to each player.
    
    # Set up the Player's chips
    players_chips = Chips()

    while playing:
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()

        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_bet(players_chips)

        # Show cards (but keep one dealer card hidden)
        print('------')
        show_some(player_hand, dealer_hand)
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exced 21, run player_bust() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, players_chips)
            # continue

        # If player hasn't busted, play dealer's hand until dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, players_chips)
            
            # dealer wins
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, players_chips)
            # player wins
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, players_chips)
            else:
                push(player_hand, dealer_hand, players_chips)
        
        # Inform Player of their chips total
        print(f'\nPlayer total chips are at: {players_chips.total}')
        # Ask to play again
        new_game = input('Would you like to player another hand? y/n: ')

        if new_game[0].lower() == 'n':
            print('Thank you for playing!')
            playing = False

    break
