import unittest
import sys
from blackjack_all_in_one import *
# from main_app import *

class CardTestCase(unittest.TestCase):
    """Unit tests for Card class"""

    def test_card_validity(self):
        with self.assertRaises(AssertionError):
            card = Card("♠", "11", 11)
        with self.assertRaises(AssertionError):
            card = Card("x", "2", 2)
        with self.assertRaises(AssertionError):
            card = Card("♦", "8", 17)

    def test_show_card(self):
        player = Role()
        computer = Role()
        player.cards = [Card("♠", "7", 7)]
        self.assertEqual(player.show_card(), "♠7")
        player.cards = [Card("♥", "A", 11), Card("♦", "Q", 10)]
        self.assertEqual(player.show_card(), "♥A♦Q")
        computer.cards = [Card("♣", "3", 3)]
        self.assertEqual(computer.show_card(), "♣3")


    def test_get_val(self):
        player = Role()
        player.cards = [Card("♦", "4", 4), Card("♣", "5", 5), Card("♣", "10", 10)]
        self.assertEqual(player.get_val('max'), 19)
        player.cards = [Card("♥", "K", 10), Card("♣", "10", 10)]
        self.assertEqual(player.get_val('max'), 20)
        player.cards = [Card("♠", "Q", 10), Card("♣", "10", 10), Card("♣", "A", 11)]
        self.assertEqual(player.get_val('max'), 21)
        player.cards = [Card("♦", "7", 7), Card("♦", "A", 11), Card("♣", "10", 10)]
        self.assertTrue(player.get_val('max'), 28)
        player.cards = [Card("♣", "A", 11), Card("♦", "A", 11), Card("♠", "J", 10)]
        self.assertEqual(player.get_val('max'), 12)
        player.cards = [Card("♣", "A", 11), Card("♣", "10", 10)]
        self.assertEqual(player.get_val('max'), 21)

    def test_bust(self):
        player = Role()
        player.cards = [Card("♦", "7", 7), Card("♦", "5", 5), Card("♣", "10", 10)]
        self.assertTrue(player.bust())
        player.cards = [Card("♦", "7", 7), Card("♦", "A", 11), Card("♣", "10", 10)]
        self.assertFalse(player.bust())

    def

    # def test_send_card(self):
    #     computer = Role()
    #     computer.cards =


 # if __name__ == '__main__':
#  #     unittest.main()