def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if row == [player, player, player]:
            return True
    
    for col in range(3):
        if [board[row][col] for row in range(3)] == [player, player, player]:
            return True
    
    if [board[i][i] for i in range(3)] == [player, player, player] or [board[i][2-i] for i in range(3)] == [player, player, player]:
        return True
    
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Cell is occupied. Try again.")
                continue
            
            board[row][col] = player
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            turn += 1
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
