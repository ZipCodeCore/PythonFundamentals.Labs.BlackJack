# Module
all_card_types = ('♠','♥','♣','♦')
all_card_texts = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
all_card_values = (11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

class Card:
    def __init__(self, card_type, card_text, card_value):
        """
        Parameters:
        card_type:str card type：（spades, hearts，clubs，diamonds）
        card_text:str ('A','J','Q','K')
        card_value:int（'A' equal 1 or 11，J, Q, K equal 10=）
        """
        assert card_type in all_card_types
        self.card_type = card_type

        assert card_text in all_card_texts
        self.card_text = card_text

        assert card_value in all_card_values
        self.card_value = card_value



