from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures.referential_array import ArrayR

from game import Game
from random_gen import RandomGen
from card import CardColor, CardLabel
from player import Player
from constants import Constants


class TestTask4(TestCase):

    @number("4.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_small_game(self) -> None:
        # Set up the small game
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 2
        players: ArrayR[Player] = ArrayR(4)
        a = Player("Alice", 0)
        b = Player("Bob", 1)
        c = Player("Charlie", 2)
        d = Player("David", 3)
        players[0] = a
        players[1] = b
        players[2] = c
        players[3] = d
        game: Game = Game()
        game.initialise_game(players)

        # Check the top card of the discard pile
        self.assertEqual(game.current_color, CardColor.GREEN, f"First card in discard pile should be GREEN, but is {game.current_color}")
        self.assertEqual(game.current_label, CardLabel.THREE, f"First card in discard pile should be THREE, but is {game.current_label}")

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(winner.name, d.name, f"Winner should be David, but is {winner.name}")

        # Check the leftover hand of Alice
        self.assertEqual(len(a), 6, f"Alice should have 6 cards left, but has {len(a)}")

        # Check the leftover hand of Bob
        self.assertEqual(len(b), 3, f"Bob should have 3 cards left, but has {len(b)}")

        # Check the leftover hand of Charlie
        self.assertEqual(len(c), 1, f"Charlie should have 1 cards left, but has {len(c)}")


    @number("4.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_long_game(self) -> None:
        # Set up the long game
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 7

        players: ArrayR[Player] = ArrayR(3)
        a = Player("Alice", 0)
        b = Player("Bob", 1)
        c = Player("Charlie", 2)

        players[0] = a
        players[1] = b
        players[2] = c
        game: Game = Game()
        game.initialise_game(players)

        # Check the top card of the discard pile
        self.assertEqual(game.current_color, CardColor.GREEN, f"First card in discard pile should be GREEN, but is {game.current_color}")
        self.assertEqual(game.current_label, CardLabel.THREE, f"First card in discard pile should be THREE, but is {game.current_label}")

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(winner.name, a.name, f"Winner should be Alice, but is {winner.name}")

        # Check the leftover hand of Bob
        self.assertEqual(len(b), 2, f"Bob should have 2 cards left, but has {len(b)}")

        # Check the leftover hand of Charlie
        self.assertEqual(len(c), 4, f"Charlie should have 4 cards left, but has {len(c)}")
