import random

def display_board(board):
    """ Display current game board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_move(board):
    """ Get the player's move and update the board"""
    # player input handling and validation
    while true: 
        try: 
            move = int(input("Enter you move(1-9):"))  -1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] == "X"
                break
            else:
                print("Invalid move! Space is already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")



def bot_move(board):
    """ Make random move for the bot"""
    # implimant bot's random move function


def main():
    """ Main function to run Tic-Tac-Toe game"""
    