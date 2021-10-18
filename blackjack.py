

import random
import os
from typing import ValuesView
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Python Blackjack
# For this project you will make a Blackjack game using Python. Click here to familiarize 
# yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, 
# but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on
#  object-oriented programming concepts.

# Rules:
# 1. The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. 
# The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13.



# Note: No wildcards will be used in the program
# 2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the 
# dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both
#  of their own cards, but should only be able to see one of the Dealer's cards.
# 3. The objective of the game is for the Player to count their cards after they're dealt. 
# If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to 
# deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. 
# A bust is when the Player is dealt cards that total more than 21.
# 4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as Blackjack. 
# Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.
# 5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. 
# A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, 
# the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
        'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit    
    

class Deck():
    def __init__(self):
        self.deck = []    
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp                


    def shuffle(self):                    
        random.shuffle(self.deck)            



    def deal(self):   
        single_card = self.deck.pop()
        return single_card

class Hand():  

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0         

    def add_card(self, card):   
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():   

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet   




def take_bet(chips): 
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("sorry! PLease type a number: ")
        else:
            if chips.bet > chips.total:
                print("Your bet cant exceed 100!")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):  
    global playing

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")
        if ask[0].lower() =='h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")    
            playing = False
        else:
            print("Sorry I did not understand that! Please try again: ")
            continue
        break

def show_some(player, dealer):
    print("\nDealers Hand: ")  
    print(" <card hidden>")
    print("", dealer.cards)
    print("\nPLayers Hand: ", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealers Hand: ", dealer.cards, sep='\n ')  
    print("Dealers Hand: ", dealer.value)
    print("\nPlayers Hand: ", player.cards, sep='\n')
    print("Players Hand =", player.value)  


# game ending
def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()



def player_wins(playes, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()  



def dealer_busts(self, chips):
    print("DEALER BUSTS!")
    chips.win_bet()    



def dealer_wins(self, chips):
    print("DEALER WINS!")
    chips.lose_bet()    


def push(self, player, dealer):  # player and dealer ties
    print("Its a push! Player and Dealer tie!")    




#gameplay

while True:
    print("Welcome to BlackJack")

    # create and shuffle deck
    deck = Deck()
    deck.shuffle()


    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    #set up players Chips
    player_chips = Chips()


    # ask player for bet
    take_bet(player_chips)

    # show cards
    show_some(player_hand, dealer_hand)

    while playing:
        # ask player to hit or stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break


            # if player hasnt busted
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        #show all cards
        show_all(player_hand, dealer_hand)


        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayers winnings stand at", player_chips.total)

    new_game = input("Would you like to play again? Wnter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break





           

    

