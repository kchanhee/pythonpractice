def sudoku(A):
    S = solveBoard(A)
    if S:
        for i in A:
            print i
    else:
        print "NO SOLUTION!"

def solveBoard(board):
    (row, col) = getUnassignedLocation(board)
    if row < 0 or col < 0:
        return True
    for num in range(1,10):
        if checkNumberValid(board, num, row, col):
            # print "current position (row, col): (%d, %d)" % (row, col)
            board[row][col] = num
            if solveBoard(board):
                return True
            board[row][col] = 0
    return False    


def getUnassignedLocation(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1) # Board is filled

def checkNumberValid(board, num, i, j):
    return checkRow(board, num, i) and checkColumn(board, num, j) and checkBox(board, num, i, j)


def checkRow(board, num, i):
    for val in board[i]:
        if num == val:
            return False
    return True

def checkColumn(board, num, j):
    for row in range(0,len(board)):
        if board[row][j] == num:
            return False
    return True

def checkBox(board, num, i, j):
    box_row = i / 3
    box_col = j / 3
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if board[row][col] == num:
                return False
    return True

for i in range(1,11):
    infile = open("%d.sd" % i)
    board = []
    for j in range(9):
        line = infile.readline().rstrip().split()
        board.append(list(map(int, line)))
    print "hello????"
    sudoku(board)


