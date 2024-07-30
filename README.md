# FIT1008-S2-2024-A1
Assignment for FIT1008/FIT2085/FIT1054 - A1

## Introduction
Welcome to the Card Game Assignment! This assignment is designed to help you learn the fundamentals of algorithms and data structures by implementing a card game. Below are the details of the game, its rules, and your tasks. Good luck and have fun!

## Game Overview
The card game involves multiple players and a deck of cards. The objective is to be the first player to get rid of all your cards. Each card has a color and a label, and there are special black cards with unique abilities.

## Important Restrictions and Assumptions

- You cannot use any built-in data structures or algorithms from any libraries except the ones provided to you in the scaffold (and no, you cannot modify the code for these data structure either).
- This means that the use of python in-built lists, dictionaries, tuples, and sets (among other built in data structures) is forbidden. - This means that the use of python in-built lists, dictionaries, tuples, and sets (among other built in data structures) is forbidden. In addition to this ArrayR is also prohibited usage of this unless provided by the scaffold will result in a penalty in approach marks.
- You cannot use any built-in sorting algorithms. You must use one of the sorting algorithms given to you in the scaffold OR use a data structure that facilitates sorting algorithms.
- You cannot use generative AI, machine learning, or any other form of AI software.
- You cannot use any hard coded constants apart from the ones provided to you in the constants class. If you need to use a constant, please add it to the constants class.
- You cannot access the internals of any data structures or any classes except the custom classes that you edit in the tasks. You can only access the methods of the data structures that are provided to you in the scaffold. Each use of the internals of a data structure will count as a major mistake and will lose at least half of the marks for the task.

## Rules of the game

1. The game is played with a deck of cards. The deck consists of 112 cards, built from four blocks of 26 cards: one block for each green, red, blue, and yellow colors. Each color has two cards of each rank (0-9), two Draw Two cards, two Skip cards,  two Reverse cards, four Crazy Crazy cards and four Crazy Draw Four cards.

2. Each player is dealt 7 cards face down (note: whether cards are face up or down will never be relevant for our set-up; we have added this info for those who know the game). The remaining cards are placed in a Draw Pile (also face down). There is also a Discard Pile where played cards are placed. The top card from the Draw Pile is then placed in the Discard Pile face up, and the game begins!

3. The player with the lowest index in the collection goes first (determined in our set-up as the player with index 0 in the array of players given as input). Play then proceeds in an increasing order of the player's index. Thus, in our set-up, we will start with the player at index 0 and move up to K where K is the number of players - 1.

4. To play a card, a player puts a card on top of the Discard Pile facing up.

5. A player can only play a card if that card is of the same color, or has the same label (number/reverse/skip) as the one at the top of the Discard Pile. Alternatively, a Crazy card, or a Crazy Draw Four card can always be played. In our set-up, the player starts scanning its cards from index 0, until they find a playable card.

6. If a player can play at least one card, they must. If they cannot, they must draw a card from the Draw Pile. If that card can be played, they must play it. Otherwise, they keep the card and the turn moves to the next player.

7. If a player plays a Crazy Crazy card, the player gets to choose the color to continue play.

8. If a player plays a Crazy Draw Four card, the color is changed to a randomly chosen color, and the next player must draw four cards from the Draw Pile and cannot play either of them. The next player must also skip their turn. The turn then moves to the player after the next player.

9. If the Draw Pile is empty, the Discard Pile (except the top card) is shuffled and placed as the new Draw Pile. (Detailed instructions on how to do this are given in Task 4.)

10. A player wins by playing all their cards. Once a player runs out of cards, the game ends immediately and that player is declared the winner. However, if the last play is a Draw Two or Draw Four card, the next player must draw the appropriate number of cards before the game ends.


## Tasks to be completed

## Task 1 - Implement the Card and Player classes

File `card.py` has two `enum` classes: `CardColor` and `CardLabel`. You must now modify it to implement the `Card` class with the following instance attributes:

- `color` - an enum value representing the color of the card.
- `label` - an enum value representing the label of the card.

You must also modify file `player.py` to implement the `Player` class with the following attributes:

- `name` - a string representing the name of the player.
- `position` - an integer representing the position of the player in the game. The player with the lowest position goes first. Positions start at 0.
- `hand` - a ordered collection of `Card` objects representing the cards in the player's hand. This list must be ordered by color of the card, then by card label in an increasing order according to the enum values. If the card has the same color and label, then consider the first card added to the hand to be the one with the lower index*.
- `add_card(self, card: Card)` - a method that takes a `Card` object as an argument and adds it to the hand. The method should return `None`. Assume that the card being passed is a valid card.
- `play_card(self, index: int)` - a method that takes an integer as an argument and removes the card at the given index from the player's hand. The method should return the card that was removed from the player's hand.
- `len(self)` - a method that returns the number of cards in the player's hand.
- `getitem(self, index: int)` - a method that takes an integer as an argument and returns the card at the given index in the player's hand.

**NOTE - For both of these classes, please add additional helper methods if you think they are necessary (including a `__str__` method to help with debugging).**

\* Our test cases will never check the order of cards with the same color and label. 


## Task 2 - The Game Class

You have been given some code in file `game.py`. You must now modify it to implement the `Game` class with the following attributes:

- `__init__(self)` - The constructor of the class. This method takes no arguments but should be used to set up the various instance variables mentioned below.

- `players` - a collection of `Player` objects representing the players in the game. The game should commence in the order of the `position` of the players. When initialising the `Game` object, this collection should be empty. You can assume that the players passed through will always be in the correct ascending order of their positions.

- `draw_pile` - a collection of `Card` objects representing the cards that players may draw to play the game. When initialising the `Game` object, this collection should be empty.

- `discard_pile` - a collection of `Card` objects representing the cards already played in the game. When initialising the `Game` object, this collection should be empty.

- `current_player` - a `Player` object representing the player whose turn it is to play. When initialising the `Game` object, this object should be empty.

- `current_color` - an `enum` value representing the color of the top card of the `discard_pile`. When initialising the `Game` object, this object should be empty.

- `current_label` - an `enum` value representing the label of the top card of the `discard_pile`. When initialising the `Game` object, this object should be empty.

- `initialise_game(self, players: ArrayR)` - This method performs the following tasks:
    1. Use the array of `Player` objects being passed to this method to populate the `players` attribute of the `Game` object.
    2. Call the method `generate_cards` to get an ArrayR of all cards
    3. Starting from card index 0 and player index 0, deal one card to each player in the order of the players. Continue to deal cards until each player has `Constants.NUM_CARDS_AT_INIT` cards in their hand.
    For example - if you have a game of 3 players with each player getting 2 cards, the players will have the following card indices in hand:
    Player 1 - 0, 3
    Player 2 - 1, 4
    Player 3 - 2, 5
    4. Continue from the index where you finished dealing the cards and add these cards to the `draw_pile`, ensuring the last index of the generated cards ends up at the top of the `draw_pile`.
    5. A card should then be drawn to be the top of the `discard_pile`. The top card of the `discard_pile` should be a number card. If the top card is a special card add it to the `discard_pile` and drew a new card. Repeat this until you get a non-special card. Special cards include anything that is not a number card.
    6. Update the `current_color` and `current_label` attributes appropriately once the top card of the `discard_pile` is a number card. Note that the `current_player` attribute remains unchanged, i.e., `None` (indicating the game has not yet started).

**NOTE - You can assume that there are at least 2 players. You can also assume that the players will not have duplicate names.**


## Task 3 - Game Components

Now that you have the basic structure of the game, it is time to implement the game logic. To do this, modify the `Game` class to implement the following methods:

- `draw_card(self, player: Player, playing: bool)` - a method that takes a `Player` object as an argument and draws a `Card` object from the `draw_pile`. If the card can be played and the `playing` argument is `True`, the card should be returned. Otherwise, the card should be added to the player's hand and the method should return `None`. This method should be called multiple times if the special card is a Draw 2 or Draw 4.

- `next_player(self)` - a method that gets the Player object of the next player (note: if `current_player` is `None`, this should simply return the Player to play the next turn). This will be helpful when you are making the next player draw cards. The method should return the `Player` object of the next player. This method should NOT update the `current_player` of the game object. This method should merely probe the next player in the order of the players.

- `play_reverse(self)` - a method that changes the direction of play. If the direction of play is clockwise, it should be changed to anti-clockwise, and vice versa. The method should return `None`.

- `play_skip(self)` - a method that skips the next player's turn. The method should return `None`.

- `crazy_play(self, card: Card)` - a method that takes a `Card` object and changes the game's `current_color` instance variable to a randomly chosen color. To choose the color, we use the following code: `CardColor(RandomGen.randint(0,3))` where `RandomGen` is an instance of the `RandomGen` class and `CardColor` is an enum class representing the colors of the cards. If its a CRAZY Draw 4 card, this method makes the next player draw 4 cards from the `draw_pile`. The method should return `None`.
  - Redundant calls to `RandomGen.randint(0,3)` will result in a loss of marks similar to as is explained with `RandomGen.random_shuffle(temp_array)` in Task 4.
  - You can assume that the card being passed is a CRAZY card.
  - Try to reuse predefined methods where possible to achieve this. Not reusing methods will result in a loss of marks.

## Task 4 - Playing the game

You must now implement the `play_game` method in the `Game` class. The `play_game` method should simulate the game. The method should return the `Player` object of the winner. The method should follow the rules of the game mentioned before and recapitulated below:

- `play_game(self)` - a method that starts the game. The game should continue until a player has no cards left in their hand. The method should return a reference to the player who won the game. You should utilise the methods defined above to achieve this method's purpose. Please remember the rules of the game! Here is a summary of the rules:
    - The player with the lowest position in the collection goes first.
      - Eg the element at the front of the queue, top of the stack, 0th index of the array, etc.
    - In our version of the game, we will be playing cards starting at index 0 and moving to the right.
    - The game ends when 1 player has no cards left in their hand.
      - The only circumstance for a game to momentarily continue is if the final card played is a Draw Two or Draw Four card, the next player must draw the appropriate number of cards before the game ends.
      - You will **not** have to consider a situation where the game ends in a draw as players have no available moves or cards to draw. All games tested will have a single winner.
    - A player can only play a card if that card has the same color or the same label as the top card of the discard pile. Alternatively, a Crazy card, or a Crazy Draw Four card can be played over any other card.
    - If a player cannot play a card, they must draw a card from the `draw_pile`. If that card can be played, they must play it. Otherwise, they keep the card and the turn moves to the next player.
    - If a player plays a draw two card, the next player must draw two cards from the Draw Pile and cannot play either of them. The next player's turn is also skipped. For example - if Bob plays Draw 2 and Charlie is the next player, Charlie must draw 2 cards from the `draw_pile` and cannot play either of them. Charlie's turn is then skipped.
    - Remember, if the draw pile is empty, the discard pile (except the top card) is shuffled and placed in the draw pile. The top card of the discard pile is then placed back on top of the discard pile. This must be done by:
        - removing the top card of the discard pile and storing it elsewhere
        - remove each card from the top of the discard pile and add it to an array
        - shuffle the array by calling `RandomGen.random_shuffle(temp_array)`
          - **Important** you must avoid redundant shuffling. If the array is already shuffled, you should not shuffle it again. **Redudant shuffling will result in your game producing different results to the expected results thus reducing your testcase marks.**
        - Start at index 0 of the shuffled array and add each card back to the draw pile, with the last index going on top of the draw pile.
        - Add the stored card back to the top of the discard pile.
    - Similarly, if a player plays a draw four card, the next player must draw four cards from the Draw Pile and cannot play either of them. The turn then moves to the next player. For example - if Bob plays Draw 4 and Charlie is the next player, Charlie must draw 4 cards from the `draw_pile` and cannot play either of them. Charlie's turn is then skipped.
    - If a player plays a CRAZY card, the player gets to choose the color to continue play. In our version of the game, we will be choosing a color using the given RandomGen class using the following code: `CardColor(RandomGen.randint(0,3))` where `RandomGen` is an instance of the `RandomGen` class and `CardColor` is an enum class representing the colors of the cards. The next player can play any card of that color or a CRAZY card.
