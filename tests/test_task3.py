from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures.referential_array import ArrayR

from game import Game
from random_gen import RandomGen
from card import CardColor, CardLabel
from player import Player
from constants import Constants
from card import Card


class TestGame(TestCase):

    def setUp(self) -> None:
        # Set seed
        RandomGen.set_seed(112)

        self.players: ArrayR[Player] = ArrayR(4)
        a = Player("Alice", 0)
        b = Player("Bob", 1)
        c = Player("Charlie", 2)
        d = Player("David", 3)
        self.players[0] = a
        self.players[1] = b
        self.players[2] = c
        self.players[3] = d

        # Set number of cards at init
        Constants.NUM_CARDS_AT_INIT = 7

        # Set up a game
        self.game: Game = Game()
        self.game.initialise_game(self.players)


    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_crazy_play(self) -> None:
        # Check the current color
        self.assertEqual(self.game.current_color, CardColor.GREEN, f"Current color should be GREEN, but is {self.game.current_color}")

        # Play a crazy card
        card: Card = Card(CardColor.CRAZY, CardLabel.CRAZY)
        self.game.crazy_play(card)

        # Check the new color
        self.assertEqual(self.game.current_color, CardColor.BLUE, f"Current color should be BLUE, but is {self.game.current_color}")

    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_crazy_draw_four(self) -> None:
        # Check the current color
        self.assertEqual(self.game.current_color, CardColor.GREEN, f"Current color should be GREEN, but is {self.game.current_color}")

        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 7, f"Alice should have 7 cards, but has {len(self.players[0])}")

        # Play a crazy card
        card: Card = Card(CardColor.CRAZY, CardLabel.DRAW_FOUR)
        self.game.crazy_play(card)

        # Check the new color
        self.assertEqual(self.game.current_color, CardColor.BLUE, f"Current color should be BLUE, but is {self.game.current_color}")

        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 11, f"Alice should have 11 cards, but has {len(self.players[0])}")

    @number("3.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card_not_playing(self) -> None:
        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 7, f"Alice should have 7 cards, but has {len(self.players[0])}")

        # Draw a card
        self.game.draw_card(self.players[0], False)

        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 8, f"Alice should have 8 cards, but has {len(self.players[0])}")

    @number("3.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card_playing(self) -> None:
        # Check current top card
        self.assertEqual(self.game.current_color, CardColor.GREEN, f"Current color should be GREEN, but is {self.game.current_color}")
        self.assertEqual(self.game.current_label, CardLabel.FIVE, f"Current label should be FIVE, but is {self.game.current_label}")

        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 7, f"Alice should have 7 cards, but has {len(self.players[0])}")

        # Draw a card (seeded to be a valid card so it can be played)
        self.game.draw_card(self.players[0], True)

        # Check the number of cards for the next player
        self.assertEqual(len(self.players[0]), 7, f"Alice should have 7 cards after playing the drawn card, but has {len(self.players[0])}")

    @number("3.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_next_player(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()

        self.assertIsInstance(next_player, Player, f"Next player should be an instance of Player, but is {type(next_player)}")
        self.assertEqual(next_player.name, "Alice", f"Next player should be Alice, but is {next_player.name}")

    @number("3.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_reverse(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(next_player.name, "Alice", f"Next player should be Alice, but is {next_player.name}")

        # Call the reverse method
        self.game.play_reverse()

        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(next_player.name, "David", f"Next player should be David, but is {next_player.name}")

    @number("3.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_skip(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(next_player.name, "Alice", f"Next player should be Alice, but is {next_player.name}")

        # Call the skip method
        self.game.play_skip()

        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(next_player.name, "Bob", f"Next player should be Bob, but is {next_player.name}")
