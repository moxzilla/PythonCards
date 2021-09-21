import itertools
import random
import numpy as np

class CardTable:
    def __init__(self,deckCount=1):
        self.deckCount = deckCount
        self.faceValue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] # all face values of cards
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.fullDeck = list(itertools.product(self.faceValue, self.suits)) # nested for loop to make combanations of face value and suit
        self.deck = []
        self.usedCards = []
        self.shuffledDeck = []
    
    def build_deck(self):
        if(self.deckCount <= 1):
            return self.fullDeck
        else:
            for x in range(self.deckCount):
                self.deck.append(self.fullDeck)
            self.fullDeck = np.concatenate(self.deck)
            self.fullDeck = self.fullDeck.tolist()
            return self.fullDeck

    def shuffle(self,times=1):  
        for p in range(times):
            shuffleOrder = random.sample(range(len(self.fullDeck)), len(self.fullDeck))
        for card in range(len(self.fullDeck)):
            self.shuffledDeck.append(self.fullDeck[shuffleOrder[card]])
        return 1
  

    def deal_one_card(self, cards=1):
        print("Card Count "+ str(len(self.shuffledDeck) - cards))
        if not self.shuffledDeck:
            print("Oh no!, there is no more cards, make another deck to play again")
            return -1
        elif(cards > 1):
            dealHand = [] 
            for x in range(cards):
                cards = self.shuffledDeck.pop(0)
                dealHand.append(cards)
            return dealHand
        else:
            card = self.shuffledDeck.pop(0)
            self.usedCards.append(card)
            return card
