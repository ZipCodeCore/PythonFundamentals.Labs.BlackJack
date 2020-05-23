import unittest
# from blackjack_all_in_one import *
from main_app import *


class CardTestCase(unittest.TestCase):

    def test_card_validity(self):
        with self.assertRaises(AssertionError):
            card = Card("♠", "11", 11)
        with self.assertRaises(AssertionError):
            card = Card("x", "2", 2)
        with self.assertRaises(AssertionError):
            card = Card("♦", "8", 17)


class RoleTestCase(unittest.TestCase):

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


class CardDealerTestCase(unittest.TestCase):

    def test_size_of_cards(self):
        dealer = CardDealer()
        self.assertEqual(len(dealer.cards), 52)


    def test_shuffle_cards(self):
        computer1 = CardDealer()
        computer2 = CardDealer()
        self.assertNotEqual(computer1.cards, computer2.cards)


    def test_deal_remove_a_card(self):
        computer = CardDealer()
        player = Role()
        num_bf = len(computer.cards)
        computer.send_card(player)
        num_af = len(computer.cards)
        self.assertEqual(num_bf, num_af + 1)


    def test_player_receive_a_card(self):
        computer = CardDealer()
        player = Role()
        player_num_bf = len(player.cards)
        computer.send_card(player)
        player_num_af = len(player.cards)
        self.assertEqual(player_num_bf, player_num_af - 1)
