import random

"""create class, each object represents a poker card 
"""


class Card:
    def __init__(self, card_type, card_text, card_value):
        """
        Parameters:
        card_type:str card type：（spades, hearts，clubs，diamonds）
        card_text:str ('A','J','Q','K')
        card_value:int（'A' equal 1 or 11，J, Q, K equal 10=）
        """
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value