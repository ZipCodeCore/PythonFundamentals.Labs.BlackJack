import unittest
import sys
# from blackjack_all_in_one import *
from main_app import *

class CardTestCase(unittest.TestCase):
    """Unit tests for Card class"""

    def test_card_validity(self):
        card = Card("♠", "7", 7)
        with self.assertRaises(AssertionError):
            card = Card("♠", "11", 11)
        with self.assertRaises(AssertionError):
            card = Card("x", "2", 2)

    def test_show_card(self):
        player = Role()
        player.cards = [Card("♠", "7", 7)]
        self.assertEqual(player.show_card(), "♠7")
        player.cards = [Card("♥", "A", 11), Card("♦", "Q", 10)]
        self.assertEqual(player.show_card(), "♥A♦Q")



