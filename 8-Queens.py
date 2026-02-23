def solve_queens(n):
    board = [-1] * n  # board[row] = column position

    def is_safe(row, col):
        for r in range(row):
            # Same column or same diagonal
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            print_solution()
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # reset

    def print_solution():
        for r in range(n):
            line = ""
            for c in range(n):
                if board[r] == c:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n" + "-" * 20)

    backtrack(0)


# Run for 8 queens
solve_queens(8)