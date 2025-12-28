# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** Connect Four (Coin Drop)

**Source:** Coinbase

**Difficulty:** Hard


# Connect Four (Coin Drop)

**Difficulty:** Hard
**Category:** Simulation, Game Logic, Arrays, Minimax / Search
**Interview Style:** Multi-stage, open-ended

---

## Problem Overview

You are asked to implement the game logic for **Connect Four**.

Connect Four is played on a **7×6 grid** (7 columns, 6 rows).
Two players alternate turns, dropping coins into columns.
A coin falls to the **lowest available cell** in the chosen column.

A player **wins** if they connect **four coins** of their color **horizontally, vertically, or diagonally**.

---

## Part 1 – Board Simulation (Core)

### Task

Implement a class `ConnectFour` that supports:

```python
game = ConnectFour()
game.drop_coin(player_id, column) -> bool
```

#### Rules

* `player_id` is either `1` or `2`
* `column` is an integer from `0` to `6`
* A coin falls to the **lowest empty row** in that column
* If the column is full, the move is invalid

#### Return

* `True` if the move was successful
* `False` if the move is invalid

---

### Example

```
drop_coin(1, 3)
drop_coin(2, 3)
drop_coin(1, 3)
```

Column `3` now contains (bottom → top):

```
[1, 2, 1]
```

---

### Constraints

* No UI
* Board stored in memory
* Moves arrive sequentially

---

## Part 2 – Win Detection

### Task

After each valid move, detect whether the current player has **won the game**.

Add:

```python
game.drop_coin(player_id, column) -> MoveResult
```

Where:

```python
MoveResult = {
    "valid": bool,
    "winner": Optional[int]
}
```

* `winner = player_id` if that move causes a win
* `winner = None` otherwise

---

### Win Conditions

You must detect:

1. Horizontal (→)
2. Vertical (↓)
3. Diagonal ()
4. Diagonal (/)

---

### Follow-up Questions (Interview Signals)

* How do you avoid scanning the entire board on every move?
* What is the **time complexity per move**?
* How would you generalize this to an `N×M` board?

---

## Part 3 – Game State Evaluation

### Task

Implement:

```python
game.is_draw() -> bool
```

A draw occurs when:

* The board is completely full
* No player has won

---

## Part 4 – Optimal Play (Hard)

### Task

Implement an **AI move selector**:

```python
game.best_move(player_id) -> int
```

Returns the column index (`0–6`) that represents the **best possible move** assuming:

* The opponent also plays optimally
* The game ends on win, loss, or draw

---

### Rules

* You may assume the board state is valid
* If multiple best moves exist, return any
* You do **not** need to finish a full game tree if pruning is applied

---

### Expectations

* Use **Minimax** (with or without alpha-beta pruning)
* Define a reasonable **heuristic evaluation** for non-terminal states
* Handle depth limits gracefully

---

### Follow-up Questions

* How would you optimize search time?
* What heuristics matter most in Connect Four?
* How would you cache repeated states?

---

## Part 5 – Scaling & Design (Optional)

### Discussion Topics

* How would you support:

  * Arbitrary board sizes?
  * More than 2 players?
  * A real-time multiplayer server?
* How would you serialize the game state?
* How would you test win detection exhaustively?

---

## What Interviewers Look For

| Skill         | Signal                           |
| ------------- | -------------------------------- |
| Simulation    | Correct gravity logic            |
| Arrays        | Clean board representation       |
| Algorithms    | Efficient win detection          |
| Design        | Extendable API                   |
| Reasoning     | Tradeoffs in minimax depth       |
| Communication | Clear explanation under pressure |

---

## Bonus Extension (Very Coinbase-ish)

> Add a method that replays a game from a move log and verifies its validity.

```python
verify_game(moves: List[int]) -> Optional[int]
```

Returns:

* `1` or `2` if a player wins
* `None` if the game is invalid or unfinished

---

If you want, next I can:

* Provide a **reference solution outline**
* Write **unit tests interviewers would use**
* Convert this into a **90-minute interview plan**
* Or make a **simplified warm-up version** first

## Approach/Pseudocode

### Initial Thoughts
For part one we want to create a ConnectFour Class that allows us to have a proper game state and a dropCoin function.

GameState would be the 7x6grid

grid = [ 0 for col in range(7) ] for row in range(6) 
Grid: 
    0, 1, 2, 3, 4, 5, 6
0.          
1
2
3
4
5.           x
       
curPlayer = 1
validPlayerIds = [1,2]
def drop_coin(player_id, column) -> bool:
    # returns valid or invalid move
    # invalid if column not in range or if column is full 
        if column < 0 or column >= 7:
            print("err: out of range)
            return False
        elif self.grid[0][column] != 0:
            print("err: column is full")
            return False
    # invalid if player_id is not turn  or out of range
        if player_id not in validPlayerIds :
            print("err: invalid PlayerId")
            return False
        if player_id == self.curPlayer
            print("err: not your turn")
            return False
    # else valid: 
        
        for i in range(ROWS): 
            if grid[i][column] != 0:
                self.grid[i-1][column] = player_id
                break
            
        return True






  
### Approach
[Describe your chosen approach in plain English. Why did you choose this method?]

### Pseudocode
```
1. [Step 1 of your algorithm]
2. [Step 2 of your algorithm]
3. [Continue with logical steps...]
4. [Final step and return]
```

### Alternative Approaches Considered
[List any other approaches you considered and why you didn't choose them]

## Edge Cases

- [ ] **Empty input:** [How does your solution handle empty arrays, strings, etc.?]
- [ ] **Single element:** [What happens with minimal input?]
- [ ] **Maximum constraints:** [How does it perform at the upper limits?]
- [ ] **Negative numbers/Invalid input:** [How do you handle unexpected input?]
- [ ] **Duplicates:** [If applicable, how do you handle duplicate values?]
- [ ] **[Custom edge case]:** [Add problem-specific edge cases]

## Time & Space Complexity

### Time Complexity
**O([your analysis])** - [Explain why this is the time complexity]

### Space Complexity  
**O([your analysis])** - [Explain the space usage, including auxiliary space]

### Optimization Notes
[Any thoughts on how this could be optimized further, or trade-offs made]

---

**Planning completed at:** 2025-12-24 11:27:24
**Estimated implementation time:** [your estimate]