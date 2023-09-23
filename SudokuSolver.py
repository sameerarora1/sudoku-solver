#August 9 Easy NYT Sudoku

sudoku_board = [
    # [0, 8, 3, 9, 1, 0, 7, 0, 0],
    # [0, 0, 6, 0, 5, 0, 0, 0, 3],
    # [0, 7, 0, 0, 0, 0, 0, 0, 0],
    # [2, 0, 9, 0, 0, 3, 0, 0, 0],
    # [0, 1, 7, 0, 0, 9, 0, 8, 0],
    # [0, 0, 0, 2, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 4, 0, 0, 5],
    # [0, 0, 0, 5, 0, 1, 0, 0, 0],
    # [8, 0, 0, 0, 0, 0, 9, 0, 6]
    # [0, 0, 2, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 2, 0, 0, 5, 0],
    # [0, 4, 0, 5, 0, 0, 0, 1, 9],
    # [0, 0, 0, 0, 8, 6, 0, 0, 1],
    # [9, 0, 0, 0, 0, 0, 0, 6, 3],
    # [0, 2, 0, 0, 0, 0, 0, 0, 5],
    # [0, 0, 3, 0, 0, 0, 0, 4, 0],
    # [0, 1, 0, 4, 0, 3, 0, 0, 0],
    # [0, 8, 7, 0, 0, 0, 0, 0, 0]
    # [0, 9, 1, 7, 0, 2, 5, 0, 0],
    # [0, 7, 4, 8, 0, 0, 2, 1, 0],
    # [8, 2, 0, 5, 9, 0, 0, 7, 6],

    # [1, 0, 0, 2, 0, 4, 0, 8, 0],
    # [0, 4, 0, 0, 0, 5, 7, 2, 1],
    # [0, 0, 7, 0, 8, 0, 0, 6, 0],

    # [7, 0, 9, 0, 0, 0, 1, 0, 3],
    # [4, 0, 0, 0, 0, 7, 0, 0, 2],
    # [3, 0, 0, 0, 5, 6, 0, 0, 0]

]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True
                        
                        board[row][col] = 0
                
                return False
    
    return True

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row[0:3], row[3:6], row[6:9])

        if sudoku_board.index(row) in [2,5]:
            print("\n")
else:
    print("No solution exists.")
