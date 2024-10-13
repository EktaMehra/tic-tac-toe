import random
import colorama

def display_board(board):
    """ Display current game board """
    for row in board:
        print(f' {" | ".join(row)} ')
        print("-" * 11)

def player_move(board):
    """ Get the player's move and update the board """
    while True:  # Fixed: "True" should be capitalized
        try: 
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"  # Fixed: use "=" for assignment
                break
            else:
                print("Invalid move! Space is already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

def bot_move(board):
    """ Make random move for the bot """
    empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_spaces:
        row, col = random.choice(empty_spaces)
        board[row][col] = "O"

def check_winner(board):
    """ Check rows, columns, and diagonals for a winner. """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None  # No winner

def check_draw(board):
    """ Check if the board is full (draw condition). """
    return all(cell != " " for row in board for cell in row)

def main():
    """ Main function to run the Tic-Tac-Toe game """
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        display_board(board)
        
        # Player's turn
        player_move(board)
        if check_winner(board):
            display_board(board)
            print("Brilliant, you win!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Bot's turn
        bot_move(board)
        if check_winner(board):
            display_board(board)
            print("Uh oh, you lose! Try again?")
            break
        if check_draw(board):
            display_board(board)
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