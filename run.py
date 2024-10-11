import random

def display_board(board):
    """ Display current game board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_move(board):
    """ Get the player's move and update the board"""
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
    empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_spaces:
        row, col = random.choice(empty_spaces)
        board[row][col] = "O"

def main():
    """ Main function to run Tic-Tac-Toe game"""
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        display_board(board)
        
        # Player's turn
        player_move(board)
        if check_winner(board):
            display_board(board)
            print("Player wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break