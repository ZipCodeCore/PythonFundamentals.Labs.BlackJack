
from random import shuffle

#Create classes for blackjack program
#This .py file will work as a module of classes
#That will be imported in the main program
#All classes will be part of this module and game willl be a separate .py program file

class Deck:
    def __init__(self):
        self = self

# A function for creating a deck
# The deck will contain cards of Suits: Heart, Spade, Diamond, Clubs  and Ranks: Ace, 2-10, Jack, Queen, King
    def deck_cards(self):
        result = []
        suit = ['H', 'S', 'D', 'C']
        num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in suit:
            for n in num:
                result.append(i+n)

# The function will return a shuffled deck with 52 cards
        shuffle(result)

        return result







# A function for creating player and dealers hands
#The player and dealer will get 2 cards initially



# A function for counting the points
# This function will count the points of the player and the dealer
# The point calculation logic will also determine the value of ACE as 1 or 11 depending on the situation

if __name__ == "__main__":
    mydeck = Deck()
    print(mydeck.deck_cards())

