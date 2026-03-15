

def create_board():
    board = []
    for i in range(6):
        rows = []
        for j in range(7):
            rows.append(" ")
        board.append(rows)
    return board
            
def print_board(board):
    
    for i in range(6):
        print("|", end="")
        for j in range(7):
            print(board[i][j], end="|")
        print()
    print(" 0 1 2 3 4 5 6")
    
def get_next_open_row(board, column):
    i = len(board) - 1
    while i >= 0:
        if board[i][column] == " ":
            return i
        i -= 1
    return None

def drop_piece(board, row, column, player):
    board[row][column] = player
    
def main():
    board = create_board()
    current_player = "O"
    
    while True:
        print_board(board)
        
        column = int(input(f"Player {current_player}, choose a column (0-6): "))
        if column < 0 or column > 6:
            print("Invalid column. Please choose a column between 0 and 6.")
            continue
        row = get_next_open_row(board, column)
        if row is None:
            print("Column is full. Please choose another column.")
            continue
        drop_piece(board, row, column, current_player)
        
        # Check for win condition here (not implemented in this code snippet)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        # Switch player
        current_player = "X" if current_player == "O" else "O"
        
def check_winner(board, player):
    # Check horizontal locations for win
    for r in range(6):
        for c in range(4):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    for c in range(7):
        for r in range(4):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
    
    for r in range(4):
        for c in range(4):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
            
    for r in range(3, 6):
        for c in range(4):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
    return False

main()