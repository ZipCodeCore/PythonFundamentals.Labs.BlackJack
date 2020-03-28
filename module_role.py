# module role
class Role:
    def __init__(self):
        """
        Create a empty list to save cards from each role (player or computer)
        """
        self.cards = []

    def show_card(self):
        for card in self.cards:
            print(card.card_type, card.card_text, sep='', end='')
        print()

    def get_val(self, max_or_min):
        """
        get the card value from each role, maximum or minimum value
        Parameters:
        max_or_min: str
            when val = max, return max. eg. 'A' equal 11, or 1 at this time
            when val = min, return min. eg. 'A' equal 1 only
        Return:
        value:int
            the value of cards in hand (max or min)
        """

        sum_cards = 0
        "The quantity of 'A' in hand"
        A = 0
        for card in self.cards:
            sum_cards += card.card_value
            # sum of quanity of 'A'
            if card.card_text == 'A':
                A += 1

        if max_or_min == "max":
            for x in range(A):
                value = sum_cards - x*10
                if value <= 21:
                    return value
        return sum_cards - A * 10

    def bust(self):
        return self.get_val('min') > 21