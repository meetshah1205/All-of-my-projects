def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        print(f"Player {current_player}, enter your move (row and column):")
        row, col = map(int, input().split())
        
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
            print("Invalid move. Try again.")
            continue
        
        board[row - 1][col - 1] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
