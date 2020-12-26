# Sudoku solver

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == -1:
                return r, c

    return False

def check_valid(board, guess, row, col):

    # check rows
    if guess in board[row]:
        return False
    
    # check columns
    for i in range(9):
        if board[i][col] == guess:
            return False

    # check 3*3 matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[row_start+i][col_start+j] == guess:
                return False
    
    return True

def solver(board):

    if find_empty(board) == False:
        return True
    
    row, col = find_empty(board)

    for guess in range(1, 10):
        if check_valid(board, guess, row, col) == True:
            board[row][col] = guess
            if solver(board) == True:
                return True
        
        board[row][col] = -1
    
    return False # unsolvable puzzle

def print_board(board):
    for r in range(9):
        for c in range(9):
            if c != 8:
                print(str(board[r][c]), end="|")
            else:
                print(str(board[r][c]))


example_board = [
    [5, 3, -1,   -1, 7, -1,   -1, -1, -1],
    [6, -1, -1,   1, 9, 5,   -1, -1, -1],
    [-1, 9, 8,   -1, -1, -1,   -1, 6, -1],

    [8, -1, -1,   -1, 6, -1,   -1, -1, 3],
    [4, -1, -1,   8, -1, 3,   -1, -1, 1],
    [7, -1, -1,   -1, 2, -1,   -1, -1, 6],

    [-1, 6, -1,   -1, -1, -1,   2, 8, -1],
    [-1, -1, -1,   4, 1, 9,   -1, -1, 5],
    [-1, -1, -1,   -1, 8, -1,   -1, 7, 9]
]

if solver(example_board) == True:
    print_board(example_board)
else:
    print("The Sudoku puzzule is unsolvable.")