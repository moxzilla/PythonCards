import itertools
import random
import numpy as np

class CardTable:
    def __init__(self,deckCount):
        self.deckCount = deckCount
        self.faceValue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] # all face 
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.colors = ["black","black","red","red"]
        self.fullDeck = list(itertools.product(self.faceValue, self.suits)) # nested for loop to make combanations of face value and suit
        self.deck = []
        self.usedCards = []
        self.shuffledDeck = []

    def build_deck(self):
        if(self.deckCount <= 1):
            print("one deck selection")
            return self.fullDeck
        else:
            print("more decks")
            for x in range(self.deckCount):
                self.deck.append(self.fullDeck)
            self.fullDeck = np.concatenate(self.deck)
            #print(len(self.deck))

    def shuffle(self,times=1):  
        #shuffleOrder = random.sample(range(len(self.fullDeck)), len(self.fullDeck))
        for p in range(times):
            shuffleOrder = random.sample(range(len(self.fullDeck)), len(self.fullDeck))
        for card in range(len(self.fullDeck)):
            self.shuffledDeck.append(self.fullDeck[shuffleOrder[card]])

    def deal_one_card(self, cards=1):
        print("card Count "+ str(len(self.shuffledDeck) - cards))
        if not self.shuffledDeck:
            print("Oh no!, there is no more cards, make another deck to play again")
            return -1
        elif(cards > 1):
            dealHand = [] 
            for x in range(cards):
                print(self.shuffledDeck.pop(0))
                #print(self.shuffledDeck[0])
                #print(len(self.shuffledDeck))
                dealHand.append(self.shuffledDeck.pop(0))
            print(dealHand)
            return dealHand
        else: 
            print(self.shuffledDeck.pop(0))


table = CardTable(1)
table.build_deck()
table.shuffle()
table.deal_one_card()

# for x in range(53):
#     table.deal_one_card()

# table.build_deck()
# table.shuffle()
# table.deal_one_card()

