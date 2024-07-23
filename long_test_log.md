# This is the log for test case 3.2

## Setup
- Set the `Player.NUM_CARDS_AT_INIT` to 7
- Set the seed `RandomGen.set_seed(123)`
- Set the players array to 3 players;
    - Alice at position 0
    - Bob at position 1
    - Charlie at position 2

## State at initialisation
This should be the state after initialising the game `g = Game(); g.initialise_game(players);`

- Top card in discard pile: GREEN THREE
- Player Alice has 7 cards. [(RED ZERO), (RED DRAW_TWO), (GREEN FOUR), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
- Player Bob has 7 cards. [(RED FOUR), (RED SEVEN), (RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
- Player Charlie has 7 cards. [(RED FIVE), (BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

## Gameplay

### Round 1
- **Current Player**: Alice
- **Top card in discard pile**: GREEN THREE
- **Action**: Alice plays GREEN FOUR

- **State**
    - Player Alice has 6 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED FOUR), (RED SEVEN), (RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(RED FIVE), (BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 2
- **Current Player**: Bob
- **Top card in discard pile**: GREEN FOUR
- **Action**: Bob plays RED FOUR

- **State**
    - Player Alice has 6 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED SEVEN), (RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(RED FIVE), (BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 3
- **Current Player**: Charlie
- **Top card in discard pile**: RED FOUR
- **Action**: Charlie plays RED FIVE

- **State**
    - Player Alice has 6 cards. Hand: [(RED ZERO), (RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED SEVEN), (RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 4
- **Current Player**: Alice
- **Top card in discard pile**: RED FIVE
- **Action**: Alice plays RED ZERO

- **State**
    - Player Alice has 5 cards. Hand: [(RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED SEVEN), (RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 5
- **Current Player**: Bob
- **Top card in discard pile**: RED ZERO
- **Action**: Bob plays RED SEVEN

- **State**
    - Player Alice has 5 cards. Hand: [(RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 5 cards. Hand: [(RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 6
- **Current Player**: Charlie
- **Top card in discard pile**: RED SEVEN
- **Action**: Charlie is unable to play any card. Charlie draws RED FOUR and plays it.

- **State**
    - Player Alice has 5 cards. Hand: [(RED DRAW_TWO), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 5 cards. Hand: [(RED NINE), (BLUE ONE), (BLUE SEVEN), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 7
- **Current Player**: Alice
- **Top card in discard pile**: RED FOUR
- **Action**: Alice plays RED DRAW_TWO. Bob draws BLUE SIX, GREEN SIX. Bob's turn is skipped.

- **State**
    - Player Alice has 4 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED NINE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW REVERSE)]

### Round 8
- **Current Player**: Charlie
- **Top card in discard pile**: RED DRAW_TWO
- **Action**: Charlie is unable to play any card. Charlie draws YELLOW EIGHT.

- **State**
    - Player Alice has 4 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED NINE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 9
- **Current Player**: Alice
- **Top card in discard pile**: RED DRAW_TWO
- **Action**: Alice is unable to play any card. Alice draws GREEN SIX.

- **State**
    - Player Alice has 5 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED NINE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 10
- **Current Player**: Bob
- **Top card in discard pile**: RED DRAW_TWO
- **Action**: Bob plays RED NINE

- **State**
    - Player Alice has 5 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 11
- **Current Player**: Charlie
- **Top card in discard pile**: RED NINE
- **Action**: Charlie is unable to play any card. Charlie draws RED ZERO and plays it.

- **State**
    - Player Alice has 5 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 12
- **Current Player**: Alice
- **Top card in discard pile**: RED ZERO
- **Action**: Alice is unable to play any card. Alice draws CRAZY DRAW_FOUR and plays it. Alice changes the color to BLUE. Bob draws RED THREE, GREEN SKIP, YELLOW ONE, YELLOW THREE. Bob's turn is skipped.

- **State**
    - Player Alice has 5 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 10 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 7 cards. Hand: [(BLUE FIVE), (BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 13
- **Current Player**: Charlie
- **Top card in discard pile**: CRAZY DRAW_FOUR
- **Action**: Charlie plays BLUE FIVE

- **State**
    - Player Alice has 5 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW FIVE), (YELLOW SEVEN)]
    - Player Bob has 10 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 14
- **Current Player**: Alice
- **Top card in discard pile**: BLUE FIVE
- **Action**: Alice plays YELLOW FIVE

- **State**
    - Player Alice has 4 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 10 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW ONE), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 15
- **Current Player**: Bob
- **Top card in discard pile**: YELLOW FIVE
- **Action**: Bob plays YELLOW ONE

- **State**
    - Player Alice has 4 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 9 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(BLUE SKIP), (GREEN ONE), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 16
- **Current Player**: Charlie
- **Top card in discard pile**: YELLOW ONE
- **Action**: Charlie plays GREEN ONE

- **State**
    - Player Alice has 4 cards. Hand: [(GREEN SIX), (GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 9 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SIX), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(BLUE SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 17
- **Current Player**: Alice
- **Top card in discard pile**: GREEN ONE
- **Action**: Alice plays GREEN SIX

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 9 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SEVEN), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(BLUE SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 18
- **Current Player**: Bob
- **Top card in discard pile**: GREEN SIX
- **Action**: Bob plays BLUE SIX

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 8 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SEVEN), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(BLUE SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 19
- **Current Player**: Charlie
- **Top card in discard pile**: BLUE SIX
- **Action**: Charlie plays BLUE SKIP. Alice's turn is skipped.

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 8 cards. Hand: [(RED THREE), (BLUE ONE), (BLUE SEVEN), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 4 cards. Hand: [(GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 20
- **Current Player**: Bob
- **Top card in discard pile**: BLUE SKIP
- **Action**: Bob plays BLUE ONE

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED THREE), (BLUE SEVEN), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 4 cards. Hand: [(GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 21
- **Current Player**: Charlie
- **Top card in discard pile**: BLUE ONE
- **Action**: Charlie is unable to play any card. Charlie draws RED SKIP.

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED THREE), (BLUE SEVEN), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 22
- **Current Player**: Alice
- **Top card in discard pile**: BLUE ONE
- **Action**: Alice is unable to play any card. Alice draws BLUE TWO and plays it.

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 7 cards. Hand: [(RED THREE), (BLUE SEVEN), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 23
- **Current Player**: Bob
- **Top card in discard pile**: BLUE TWO
- **Action**: Bob plays BLUE SEVEN

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED THREE), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 24
- **Current Player**: Charlie
- **Top card in discard pile**: BLUE SEVEN
- **Action**: Charlie is unable to play any card. Charlie draws RED THREE

- **State**
    - Player Alice has 3 cards. Hand: [(GREEN SEVEN), (GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED THREE), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(RED THREE), (RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 25
- **Current Player**: Alice
- **Top card in discard pile**: BLUE SEVEN
- **Action**: Alice plays GREEN SEVEN

- **State**
    - Player Alice has 2 cards. Hand: [(GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 6 cards. Hand: [(RED THREE), (GREEN SIX), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(RED THREE), (RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 26
- **Current Player**: Bob
- **Top card in discard pile**: GREEN SEVEN
- **Action**: Bob plays GREEN SIX

- **State**
    - Player Alice has 2 cards. Hand: [(GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 5 cards. Hand: [(RED THREE), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 6 cards. Hand: [(RED THREE), (RED SKIP), (GREEN TWO), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 27
- **Current Player**: Charlie
- **Top card in discard pile**: GREEN SIX
- **Action**: Charlie plays GREEN TWO

- **State**
    - Player Alice has 2 cards. Hand: [(GREEN NINE), (YELLOW SEVEN)]
    - Player Bob has 5 cards. Hand: [(RED THREE), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 28
- **Current Player**: Alice
- **Top card in discard pile**: GREEN TWO
- **Action**: Alice plays GREEN NINE

- **State**
    - Player Alice has 1 cards. Hand: [(YELLOW SEVEN)]
    - Player Bob has 5 cards. Hand: [(RED THREE), (GREEN SKIP), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 29
- **Current Player**: Bob
- **Top card in discard pile**: GREEN NINE
- **Action**: Bob plays GREEN SKIP. Charlie's turn is skipped.

- **State**
    - Player Alice has 1 cards. Hand: [(YELLOW SEVEN)]
    - Player Bob has 4 cards. Hand: [(RED THREE), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 30
- **Current Player**: Alice
- **Top card in discard pile**: GREEN SKIP
- **Action**: Alice is unable to play any card. Alice draws RED EIGHT

- **State**
    - Player Alice has 2 cards. Hand: [(RED EIGHT), (YELLOW SEVEN)]
    - Player Bob has 4 cards. Hand: [(RED THREE), (YELLOW THREE), (YELLOW FIVE), (YELLOW SKIP)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 31
- **Current Player**: Bob
- **Top card in discard pile**: GREEN SKIP
- **Action**: Bob plays YELLOW SKIP. Charlie's turn is skipped.

- **State**
    - Player Alice has 2 cards. Hand: [(RED EIGHT), (YELLOW SEVEN)]
    - Player Bob has 3 cards. Hand: [(RED THREE), (YELLOW THREE), (YELLOW FIVE)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 32
- **Current Player**: Alice
- **Top card in discard pile**: YELLOW SKIP
- **Action**: Alice plays YELLOW SEVEN

- **State**
    - Player Alice has 1 cards. Hand: [(RED EIGHT)]
    - Player Bob has 3 cards. Hand: [(RED THREE), (YELLOW THREE), (YELLOW FIVE)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 33
- **Current Player**: Bob
- **Top card in discard pile**: YELLOW SEVEN
- **Action**: Bob plays YELLOW THREE

- **State**
    - Player Alice has 1 cards. Hand: [(RED EIGHT)]
    - Player Bob has 2 cards. Hand: [(RED THREE), (YELLOW FIVE)]
    - Player Charlie has 5 cards. Hand: [(RED THREE), (RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 34
- **Current Player**: Charlie
- **Top card in discard pile**: YELLOW THREE
- **Action**: Charlie plays RED THREE.

- **State**
    - Player Alice has 1 cards. Hand: [(RED EIGHT)]
    - Player Bob has 2 cards. Hand: [(RED THREE), (YELLOW FIVE)]
    - Player Charlie has 4 cards. Hand: [(RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

### Round 35
- **Current Player**: Alice
- **Top card in discard pile**: RED THREE
- **Action**: Alice plays RED EIGHT. Alice wins.

- **State**
    - Player Alice has 0 cards. Hand: []
    - Player Bob has 2 cards. Hand: [(RED THREE), (YELLOW FIVE)]
    - Player Charlie has 4 cards. Hand: [(RED SKIP), (YELLOW ZERO), (YELLOW EIGHT), (YELLOW REVERSE)]

## End of Game