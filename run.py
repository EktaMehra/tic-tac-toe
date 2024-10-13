import random
import os
import colorama
from colorama import Fore, Back, Style

# Initialize Colorama for cross-platform color support
colorama.init(autoreset=True)

class Game:
    def __init__(self):
        """ Initialize the game board and player symbols """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player_symbol = ""
        self.bot_symbol = ""

    def display_board(self):
        """ Display the current game board with color formatting """
        for row in self.board:
            colored_row = [self.get_colored_cell(cell) for cell in row]
            print(f' {colored_row[0]} | {colored_row[1]} | {colored_row[2]} ')
            print("-" * 11)

    def get_colored_cell(self, cell):
        """ Return the cell with appropriate color and white background """
        if cell == "X":
            return Back.WHITE + Fore.CYAN + cell + Style.RESET_ALL  # Cyan X with white background
        elif cell == "O":
            return Back.WHITE + Fore.RED + cell + Style.RESET_ALL  # Red O with white background
        return Back.WHITE + cell + Style.RESET_ALL  # Empty spaces with white background

    def player_move(self):
        """ Get the player's move and update the board """
        while True:
            try:
                move = int(input(f"Enter your move (1-9), {self.player_symbol}: ")) - 1
                row, col = divmod(move, 3)
                if self.board[row][col] == " ":
                    self.board[row][col] = self.player_symbol
                    break
                else:
                    print("Invalid move! Space is already taken.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")

    def bot_move(self):
        """ Make a random move for the bot """
        empty_spaces = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_spaces:
            row, col = random.choice(empty_spaces)
            self.board[row][col] = self.bot_symbol

    def check_winner(self):
        """ Check rows, columns, and diagonals for a winner """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None  # No winner

    def check_draw(self):
        """ Check if the board is full (draw condition) """
        return all(cell != " " for row in self.board for cell in row)

    def choose_symbol(self):
        """ Let the player choose whether they want to play as 'X' or 'O' """
        while True:
            choice = input("Do you want to be 'X' or 'O'? ").upper()
            if choice in ["X", "O"]:
                self.player_symbol = choice
                self.bot_symbol = "O" if choice == "X" else "X"
                break
            else:
                print("Invalid choice. Please choose 'X' or 'O'.")

    def clear_terminal(self):
        """ Clear the terminal screen (works for both Windows and Unix-based systems) """
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """ Main function to run the Tic-Tac-Toe game """
    game = Game()
    game.choose_symbol()

    while True:
        game.clear_terminal()  # Clear the screen before displaying the board
        game.display_board()

        # Player's turn
        game.player_move()
        if game.check_winner():
            game.clear_terminal()
            game.display_board()
            print(f"Brilliant, {game.player_symbol} wins!")
            break
        if game.check_draw():
            game.clear_terminal()
            game.display_board()
            print("It's a draw!")
            break

        # Bot's turn
        game.bot_move()
        if game.check_winner():
            game.clear_terminal()
            game.display_board()
            print(f"Uh oh, {game.bot_symbol} wins! Try again?")
            break
        if game.check_draw():
            game.clear_terminal()
            game.display_board()
            print("It's a draw!")
            break

    print("Game over. Thanks for playing!")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        main()
    else:
        print("Exiting game...")

if __name__ == "__main__":
    main()
