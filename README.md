## Tic-tac-toe (4x4)

This is a 4x4 Tic-tac-toe solver implemented in Python. It includes the core game logic for checking winners and managing game states. Note that the input UI is not implemented yet.

### Features

- Functions to check for winning conditions (vertical, horizontal, diagonal, 4 corners, 2x2 boxes)
- Function to check if any moves are left
- Function to determine if the game is over

### How to play
- Execute the script by running the following command in your terminal or command prompt:
  ```bash
  python tictactoe.py
  ```
- When prompted, enter the current state of the board.
    - The board is a 4x4 grid where:
        - `0` represents an empty cell
        - `1` represents the first player's move
        - `2` represents the second player's move
    - Enter the board row by row, separating each cell value with a space. For example:
      ```
      0 1 0 2
      1 0 2 0
      0 2 1 0
      2 0 1 0
      ```

      ```
      1 2 1 2
      2 1 1 1
      1 2 2 2
      2 1 2 1
      ```

      ```
      1 2 2 1
      0 0 0 0
      0 0 0 0
      1 0 2 1
      ```
- The script will evaluate the board and determine the game state:
    - If there is a winner, it will print either "First player wins!" or "Second player wins!".
    - If the game is a tie (no moves left and no winner), it will print "Tie".
    - If the game is not yet over (there are still moves left and no winner), it will print "Continue".


### Requirements

- Python 3.9+
