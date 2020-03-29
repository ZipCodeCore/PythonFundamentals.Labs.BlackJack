import random
import time
import sys
from module_card import *
from module_role import Role


class CardDealer:
    def __init__(self):
        self.cards = []

        for card_type in all_card_types:
            for index, card_text in enumerate(all_card_texts):
                card = Card(card_type, card_text, all_card_values[index])
                self.cards.append(card)

        #cards shuffle
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
    """
    Game start, comupter will show value of one card, player show value of two cards
    """
    cards.send_card(computer, num=1)
    cards.send_card(player, num=2)
    print(computer.show_card())
    print(player.show_card())

    # Ask player to send cards, if player hit, cointue, if player stand, stop
    while (True):
        choice = input('Hit or Stand? (H/S)\n')
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

    # When player stand, if dealer value is less than 17, will continue hit, if value between 17 ~ 21, stop
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
