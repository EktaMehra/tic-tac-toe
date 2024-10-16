# Tic-Tac-Toe Game
Play the [Tic-Tac-Toe Game](https://tictactoe-em-45ad1fa00a31.herokuapp.com/) here.
## Introduction
This is a simple Python implementation of the classic Tic-Tac-Toe game. The game is played between a human player and a bot. The goal is to align three of your symbols (X or O) in a row, column, or diagonal on a 3x3 grid. The game ends when a player wins or when the grid is completely filled (resulting in a draw).
![Responsive screen image](assets/tictactoe%20responsive%20screen.PNG)

## How to Play
- The game is played on a 3x3 grid, initially empty.
- The player will be prompted to select their symbol, "X" or "O".
- They enter their move by selecting a number between 1 and 9, which corresponds to a position on the grid.
- The bot will then make its move, selecting a random empty space.
- The game alternates between the player and the bot until either: the player wins by getting three of their symbols in a row (horizontal, vertical, or diagonal) or the board is filled and results in a draw.
- At the end of the game, the winner or the draw status will be announced, and the player can choose to play again or exit the game.

## Planning
The planning draft of the game's structure.
![Planning flowchart of the game](assets/tictactoe%20planning.PNG)

## Features
### Existing Features:
1. Player vs Bot: The player plays against a basic bot that randomly selects available moves.
2. Player Move: Players can now choose whether to play as X or O before the game begins.The game will prompt the player to select their symbol, and the computer will automatically be assigned the other symbol. Players input a number between 1 and 9 to make their move, representing positions on the 3x3 grid. The game will validate the move to ensure the chosen position is empty. Invalid moves will prompt the player to enter a valid number.
3. Symbol Selection: The player can pick if they want to play as "X" or "O".
![tictactoe start](assets/tictactoe%20game0.PNG)
4. Winner and Draw Detection: The game checks for both winning and draw conditions after every move.
5. Replay Option: After the game ends, the player can choose to play again or exit.
6. Colorama: Added this feature to make the board more attractive and accessible
![tictactoe color theme](assets/tictactoe%20game1.PNG)

### Future Features:
1. Improved AI: Implementing a smarter bot using the minimax algorithm to challenge the player more effectively.
2. Multiplayer Mode: Allow two human players to play against each other.
Graphical User Interface (GUI): Develop a graphical version of the game using a library like Tkinter or Pygame.
3. Scoreboard: Track and display scores across multiple games.
## Data Model
The game uses a 2D list (3x3 matrix) to represent the game board. Each cell in the grid is either empty (" "), contains the player's symbol ("X"), or contains the bot's symbol ("O"). The indices of the grid correspond to the following positions:

### 1 | 2 | 3
-----
### 4 | 5 | 6
-----
### 7 | 8 | 9

The player selects a number (1-9) to place their symbol, which is then converted into the corresponding row and column on the board.

## Testing
### Manual Testing:
1. Player Move Validations: Ensured that invalid moves (e.g., selecting an already filled space or entering out-of-range numbers) are rejected with appropriate prompts.
2. Win and Draw Conditions: Tested different board states to confirm that the game accurately detects wins in all rows, columns, and diagonals, as well as draw conditions.
3. Bot Move Functionality: Ensured that the bot selects a random valid move and updates the board correctly.
### Automated Testing (Future):
Future plans include adding unit tests to verify the correctness of key functions such as move validation, win checking, and board display.
## Bugs
### Known Bugs:
1. Bot Move Optimization: The bot currently selects a move randomly, which can sometimes lead to unintelligent gameplay. This is slated for future improvement.
2. Occasional input validation edge cases: If the player enters non-numeric input, the program may throw a ValueError. Additional input checks are planned to handle such cases more gracefully.
### Fixed Bugs:
1. Fixed an issue where the player’s symbol wasn't being assigned correctly on the board due to the use of comparison (==) instead of assignment (=).
2. Addressed an issue where the game would fail to prompt the player again after an invalid input.
## Validator Testing
PEP8 : No errors were returned from [PEP8ci.herokuapp.com](https://pep8ci.herokuapp.com/)
## Deployment
This project was deployed using Code Institute's mock terminal for Heroku and some [Google](www.google.com) research:
- Add a line "worker: python tictactoe.py" to Procfile
- Create new Heroku app
- Set the buildbacks to python and NodeJS in that order
- Link Heroku app to repository
- Click on deploy

## Credits
1. Game Inspiration: The classic game of Tic-Tac-Toe.
2. Reference Repository: [ImKennyYip's Tic-Tac-Toe Python](https://github.com/ImKennyYip/tictactoe-python) provided inspiration for structuring the project and implementing core features.