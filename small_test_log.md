# This is the log for test case 3.1

## Setup
- Set the `Player.NUM_CARDS_AT_INIT` to 2
- Set the seed `RandomGen.set_seed(123)`
- Set the players array to 4 players;
    - Alice at position 0
    - Bob at position 1
    - Charlie at position 2
    - David at position 3

## State at initialisation
This should be the state after initialising the game `g = Game(); g.initialise_game(player);`

- Top card in discard pile: GREEN THREE
- Player Alice has 2 cards. RED ZERO; YELLOW FIVE;
- Player Bob has 2 cards. BLUE FIVE; YELLOW SKIP;
- Player Charlie has 2 cards. RED DRAW_TWO; BLUE SKIP;
- Player David has 2 cards. RED NINE; GREEN NINE;

## Gameplay

### Round 1
- **Current Player**: Alice
- **Top card in discard pile**: GREEN THREE
- **Action**: Alice is unable to play any card. Alice draws RED FOUR

- **State**
    - Player Alice has 3 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE)]
    - Player Bob has 2 cards. Hand: [(BLUE FIVE), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 2 cards. Hand: [(RED NINE), (GREEN NINE)]


### Round 2
- **Current Player**: Bob
- **Top card in discard pile**: GREEN THREE
- **Action**: Bob is unable to play any card. Bob draws BLUE SIX

- **State**
    - Player Alice has 3 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE)]
    - Player Bob has 3 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 2 cards. Hand: [(RED NINE), (GREEN NINE)]

### Round 3

- **Current Player**: Charlie
- **Top card in discard pile**: GREEN THREE
- **Action**: Charlie is unable to play any card. Charlie draws GREEN SIX and plays it.

- **State**
    - Player Alice has 3 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE)]
    - Player Bob has 3 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 2 cards. Hand: [(RED NINE), (GREEN NINE)]

### Round 4
- **Current Player**: David
- **Top card in discard pile**: GREEN SIX
- **Action**: David plays GREEN NINE

- **State**
    - Player Alice has 3 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE)]
    - Player Bob has 3 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 5
- **Current Player**: Alice
- **Top card in discard pile**: GREEN NINE
- **Action**: Alice is unable to play a card. Alice draws YELLOW EIGHT

- **State**
    - Player Alice has 4 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 3 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 6
- **Current Player**: Bob
- **Top card in discard pile**: GREEN NINE
- **Action**: Bob is unable to play a card. Bob draws GREEN SIX and plays it.

- **State**
    - Player Alice has 4 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 4 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 7
- **Current Player**: Charlie
- **Top card in discard pile**: GREEN SIX
- **Action**: Charlie is unable to play a card. Charlie draws RED ZERO

- **State**
    - Player Alice has 4 cards. Hand: [(RED ZERO), (RED FOUR), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 4 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 3 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 8
- **Current Player**: David
- **Top card in discard pile**: GREEN SIX
- **Action**: David is unable to play a card. David draws CRAZY DRAW_FOUR and plays it. The current color is BLUE
Alice draws RED THREE, GREEN SKIP, YELLOW ONE, YELLOW THREE. Alice loses her turn.

- **State**
    - Player Alice has 8 cards. Hand: [(RED ZERO), (RED THREE), (RED FOUR), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 3 cards. Hand: [(BLUE FIVE), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 3 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 9
- **Current Player**: Bob
- **Top card in discard pile**: CRAZY DRAW_FOUR
- **Action**: Bob plays BLUE FIVE

- **State**
    - Player Alice has 8 cards. Hand: [(RED ZERO), (RED THREE), (RED FOUR), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 2 cards. Hand: [(BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 3 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (BLUE SKIP)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 10
- **Current Player**: Charlie
- **Top card in discard pile**: BLUE FIVE
- **Action**: Charlie plays BLUE SKIP. David's turn is skipped.

- **State**
    - Player Alice has 8 cards. Hand: [(RED ZERO), (RED THREE), (RED FOUR), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 2 cards. Hand: [(BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED ZERO), (RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 11
- **Current Player**: Alice
- **Top card in discard pile**: BLUE SKIP
- **Action**: Alice plays GREEN SKIP. Bob's turn is skipped.

- **State**
    - Player Alice has 7 cards. Hand: [(RED ZERO), (RED THREE), (RED FOUR), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 2 cards. Hand: [(BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED ZERO), (RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 12
- **Current Player**: Charlie
- **Top card in discard pile**: GREEN SKIP
- **Action**: Charlie is unable to play a card. Charlie draws RED SKIP and plays it. David's turn is skipped.

- **State**
    - Player Alice has 7 cards. Hand: [(RED ZERO), (RED THREE), (RED FOUR), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 2 cards. Hand: [(BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED ZERO), (RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 13
- **Current Player**: Alice
- **Top card in discard pile**: RED SKIP
- **Action**: Alice plays RED ZERO

- **State**
    - Player Alice has 6 cards. Hand: [(RED THREE), (RED FOUR), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 2 cards. Hand: [(BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED ZERO), (RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 14
- **Current Player**: Bob
- **Top card in discard pile**: RED ZERO
- **Action**: Bob is unable to play a card. Bob draws BLUE TWO

- **State**
    - Player Alice has 6 cards. Hand: [(RED THREE), (RED FOUR), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 3 cards. Hand: [(BLUE TWO), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 2 cards. Hand: [(RED ZERO), (RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 15
- **Current Player**: Charlie
- **Top card in discard pile**: RED ZERO
- **Action**: Charlie plays RED ZERO

- **State**
    - Player Alice has 6 cards. Hand: [(RED THREE), (RED FOUR), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW EIGHT)]
    - Player Bob has 3 cards. Hand: [(BLUE TWO), (BLUE SIX), (YELLOW SKIP)]
    - Player Charlie has 1 cards. Hand: [(RED DRAW_TWO)]
    - Player David has 1 cards. Hand: [(RED NINE)]

### Round 16
- **Current Player**: David
- **Top card in discard pile**: RED ZERO
- **Action**: David plays RED NINE. David wins the game.


## End of Game