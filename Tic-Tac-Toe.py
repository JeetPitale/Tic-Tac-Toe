# 🎮 Tic Tac Toe Game
# Author: Jeet Pitale
# Simple 2-player command-line Tic Tac Toe game in Python

# Function to print the board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)

# Function to check for a draw
def check_draw(board):
    return " " not in board

# Main game loop
def play_game():
    board = [" "] * 9
    current_player = "X"
    game_running = True

    print("Welcome to 🎮 Tic Tac Toe!")
    print("Positions are as follows:")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

    while game_running:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("⚠️ Invalid move. Choose a number between 1 and 9.")
                continue

            if board[move] == " ":
                board[move] = current_player
                if check_win(board, current_player):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins!")
                    game_running = False
                elif check_draw(board):
                    print_board(board)
                    print("🤝 It's a draw!")
                    game_running = False
                else:
                    # Switch player
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("⚠️ Spot already taken. Try again.")

        except ValueError:
            print("⚠️ Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_game()
