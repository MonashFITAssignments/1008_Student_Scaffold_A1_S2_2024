from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures.referential_array import ArrayR

from game import Game
from random_gen import RandomGen
from card import Card, CardColor, CardLabel
from player import Player
from constants import Constants


class TestGame(TestCase):

    def setUp(self) -> None:
        self.players: ArrayR[Player] = ArrayR(4)
        self.players[0] = Player("Alice", 0)
        self.players[1] = Player("Bob", 1)
        self.players[2] = Player("Charlie", 2)
        self.players[3] = Player("David", 3)

    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_game_init(self):
        game: Game = Game()
        self.assertTrue(hasattr(game, "draw_pile"), f"draw_pile not found in game, please ensure your spelling is correct")
        self.assertTrue(hasattr(game, "discard_pile"), f"discard_pile not found in game, please ensure your spelling is correct")
        self.assertEqual(game.current_color, None, f"current_color should be None after initialising the game")
        self.assertEqual(game.current_label, None, f"current_label should be None after initialising the game")

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_after_initialise_game(self) -> None:
        Constants.NUM_CARDS_AT_INIT = 7
        game: Game = Game()
        game.initialise_game(self.players)
        self.assertLessEqual(len(game.draw_pile), 83, f"There should be at most 83 cards in the unused pile, but there are {len(game.draw_pile)}")
        self.assertGreaterEqual(len(game.discard_pile), 1, f"There should be at least 1 card in the discard pile, but there are {len(game.discard_pile)}")
        self.assertNotEqual(game.current_color, None, f"current_color should not be None after initialising the game")
        self.assertNotEqual(game.current_label, None, f"current_label should not be None after initialising the game")

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_initialise_game_with_3_players(self) -> None:
        Constants.NUM_CARDS_AT_INIT = 7
        game: Game = Game()
        game.initialise_game(self.players[0:3])
        self.assertLessEqual(len(game.draw_pile), 90, f"There should be at most 90 cards in the unused pile, but there are {len(game.draw_pile)}")
        self.assertGreaterEqual(len(game.discard_pile), 1, f"There should be at least 1 card in the discard pile, but there are {len(game.discard_pile)}")
        self.assertNotEqual(game.current_color, None, f"current_color should not be None after initialising the game")
        self.assertNotEqual(game.current_label, None, f"current_label should not be None after initialising the game")

    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_seeded_random_result(self) -> None:
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 7
        game: Game = Game()
        game.initialise_game(self.players)

        # Check the first card in the unused pile
        self.assertEqual(game.draw_pile.array[0].color, CardColor.BLUE, f"First card in unused pile should be BLUE, but is {game.draw_pile.array[0].color}")
        self.assertEqual(game.draw_pile.array[0].label, CardLabel.DRAW_TWO, f"First card in unused pile should be DRAW_TWO, but is {game.draw_pile.array[0].label}")

        # Check the first card in the hand of the first player
        self.assertEqual(game.players.array[0].hand[0].color, CardColor.RED, f"First card in first player's hand should be RED, but is {game.players.array[0].hand[0].color}")
        self.assertEqual(game.players.array[0].hand[0].label, CardLabel.ZERO, f"First card in first player's hand should be ZERO, but is {game.players.array[0].hand[0].label}")
