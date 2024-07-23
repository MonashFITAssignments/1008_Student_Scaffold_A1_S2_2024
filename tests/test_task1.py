from unittest import TestCase
from card import Card, CardColor, CardLabel
from player import Player
from ed_utils.decorators import number, visibility


class TestTask1(TestCase):

    def setUp(self) -> None:
        self.player: Player = Player("Player 1", 0)

    # Test the card's init has been set up correctly
    @number("1.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_card_init(self) -> None:
        card: Card = Card(CardColor.RED, CardLabel.ONE)
        self.assertEqual(card.color, CardColor.RED)
        self.assertEqual(card.label, CardLabel.ONE)

    @number("1.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_card_init_2(self) -> None:
        # Test CRAZY cards
        card: Card = Card(CardColor.CRAZY, CardLabel.CRAZY)
        self.assertEqual(card.color, CardColor.CRAZY)
        self.assertEqual(card.label, CardLabel.CRAZY)

    @number("1.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_init(self) -> None:
        self.assertEqual(len(self.player), 0)
        self.assertEqual(len(self.player.hand), 0)

    @number("1.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_add_card(self) -> None:
        card: Card = Card(CardColor.RED, CardLabel.ONE)
        self.player.add_card(card)
        self.assertEqual(len(self.player), 1)
        self.assertEqual(len(self.player.hand), 1)

    @number("1.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_card(self) -> None:
        card: Card = Card(CardColor.RED, CardLabel.ONE)
        self.player.add_card(card)
        self.assertEqual(len(self.player), 1)
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(self.player.play_card(0), card)
        self.assertEqual(len(self.player), 0)
        self.assertEqual(len(self.player.hand), 0)
