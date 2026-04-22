def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row):
    if row == len(board):
        print(board)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)

board = [0] * 8
solve(board, 0)