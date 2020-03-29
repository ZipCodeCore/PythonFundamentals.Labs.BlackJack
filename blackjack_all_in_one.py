import random
import time
import sys

all_card_types = '♠♥♣♦'
all_card_texts = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
all_card_values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

class Card():
    def __init__(self, card_type, card_text, card_value):
        """
        Parameters:
        card_type:str card type：（spades, hearts，clubs，diamonds）
        card_text:str ('A','J','Q','K','10', '9', '8', '7', '6', '5', '4', '3', '2', '1')
        card_value:int（'A' equal 1 or 11，J, Q, K equal 10）
        """
        assert card_type in all_card_types
        self.card_type = card_type

        assert card_text in all_card_texts
        self.card_text = card_text

        assert card_value in all_card_values
        self.card_value = card_value


class Role():
    def __init__(self):
        """
        Create a empty list to save cards from each role (player or computer)
        """
        self.cards = []

    def show_card(self):
        return (''.join([''.join([card.card_type, card.card_text]) for card in self.cards]))
        # for card in self.cards:
            # print(card.card_type, card.card_text, sep='', end='')
        #print()


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


class CardDealer():
    def __init__(self):
        self.cards = []

        for card_type in all_card_types:
            for index, card_text in enumerate(all_card_texts):  
                card = Card(card_type, card_text, all_card_values[index])
                self.cards.append(card)

        random.shuffle(self.cards)

    def send_card(self, role, num = 1):
        """
        Send card to player or computer
        Parameters:
        role: Role
        num: int
            send just one card
        """

        for i in range(num):
            card = self.cards.pop()
            role.cards.append(card)


cards = CardDealer()
computer = Role()
player = Role()


if __name__ == '__main__':
    # Game start
    # Ask player to send cards, if player hit, continue, if player stand, stop
    # Comupter will show value of one card, player show value of two cards
    cards.send_card(computer, num=1)
    cards.send_card(player, num=2)
    print(computer.show_card())
    print(player.show_card())
    # computer.show_card()
    # player.show_card()
    while (True):
        choice = input('Hit or Stand? (H/S)')
        if choice.upper() == 'H':
            cards.send_card(player)
            print(computer.show_card())
            print(player.show_card())

            if player.bust():
                print('Player bust! You lost!')
                sys.exit()
        elif choice.upper() == 'S':
            break
        else:
            print('Invalid input, please enter: H/S')
            choice

    # When player stand, if dealer value is less than 17,
    # will continue hit, if value between 12 ~ 21, stop
    while (True):
        print('Dealing......')
        # set a time gap here to send card
        time.sleep(1)
        cards.send_card(computer)
        print(computer.show_card())
        print(player.show_card())
        if computer.bust():
            print('Dealer bust! You win!')
            sys.exit()
        elif computer.get_val('max') >= 17:
            break

    player_val = player.get_val('max')
    computer_val = computer.get_val('max')

    if player_val > computer_val:
        print('You win!')
    elif player_val == computer_val:
        print('Push!')
    else:
        print('You lost!')