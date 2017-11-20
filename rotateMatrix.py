
def rotateMatrix(A):
    n = len(A)
    for layer in range(n / 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # top
            top = A[first][i]
            # left -> top
            A[first][i] = A[last - offset][first]
            # bottom -> left
            A[last - offset][first] = A[last][last-offset]
            # right -> bottom 
            A[last][last - offset] = A[i][last]
            # top -> right
            A[i][last] = top
    return A

def printMat(A):
    for i in range(len(A)):
        print A[i]


A1 = [[1, 2, 3, 4, 5],
     [3, 4, 5, 6, 7],
     [4, 5, 1, 3, 9],
     [3, 4, 5, 2, 1],
     [1, 2, 4, 2, 6]]

A2 = [[1, 3, 4, 2],
      [2, 5, 4, 1],
      [4, 1, 8, 3],
      [9, 8, 7, 2]]

printMat(rotateMatrix(A1))
printMat(rotateMatrix(A2))