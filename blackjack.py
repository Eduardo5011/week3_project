

import random
import os
from typing import ValuesView
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    print("\nPLayers Hand: ", *player.cards)


def show_all(player, dealer):
    print("\nDealers Hand: ", dealer.cards)  
    print("Dealers Hand: ", dealer.value)
    print("\nPlayers Hand: ", player.card)
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


def push(self, player, dealer):  
    print("Its a push! Player and Dealer tie!")    






while True:
    print("Welcome to BlackJack")

    deck = Deck()
    deck.shuffle()


    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    
    player_chips = Chips()


    
    take_bet(player_chips)

    
    show_some(player_hand, dealer_hand)

    while playing:
       
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break


            
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
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





           

    

