# Given Matrix A filled with positive integers
# Find the largest sub-matrix with filled with the same values
areaDict = {}
def getmatrix(file):
    A = []
    with open(file) as f:
        line = f.readline()
        while line != "":
            res = map(int, line.split(' '))
            A.append(res)
            line = f.readline()
    return A

def getMaxRect(A):

    (r,c) = findNextLocation(A)
    # print '(r,c) = (%d, %d)' % (r,c)
    if r < 0 or c < 0:
        return 0
    N = A[r][c]
    if len(A) == 0:
        return 0
    if len(A) == 1 and len(A[0]) == 1:
        return 1
    # printMat(A)
    x = getArea(A,r,c,N)
    if N in areaDict:
        if x > areaDict[N]:
            areaDict[N] = x
    else:
        areaDict[N] = x
    return max(x, getMaxRect(A))

def getArea(A,r,c,N):
    if len(A) == 1:
        return getLongestCol(A,r,c,N)

    rL = getLongestRow(A,r,c,N)
    cL = getLongestCol(A,r,c,N)
    # print 'Given N = %d, (longest row, longest col) = %d, %d' % (N, rL, cL)
    if rL < cL:
        for i in range(r, r + rL):
            cNL = getLongestCol(A, i, c, N)
            # print 'new Longest column: %d' % cNL
            if cNL < cL:
                cL = cNL
    if cL <= rL:
        for j in range(c, c + cL):
            rNL = getLongestRow(A, r, j, N)
            # print 'new Longest row: %d' % rNL
            if rNL < rL:
                rL = rNL

    return (rL) * (cL)


def findNextLocation(A):
    for r in range(len(A)):
        for c in range(len(A[r])):
            # print A[r][c]
            if A[r][c] > 0:
                return (r,c)
    return (-1,-1)


def getLongestRow(A, r, c, N):
    for i in range(r, len(A)):
        if abs(A[i][c]) != abs(N):
            return i - r
        else:
            A[i][c] = -abs(N)
    else:
        return i - r + 1

def getLongestCol(A, r, c, N):

    for i in range(c, len(A[r])):
        if abs(A[r][i]) != abs(N):
            return i - c 
        else:
            A[r][i] = -abs(N)
    else:
        return i - c + 1

def printMat(A):
    for i in A:
        print i

A = getmatrix('m1.sd')
B = A
X = getMaxRect(A)
print "For Matrix A: " 
printMat(B)
# print areaDict
for i in areaDict.keys():
    if areaDict[i] == X:
        print "%d has the largest area with %d" % (i, X)        
areaDict = {}

L = []
for i in range(10):
    l = []
    for j in range(10):
        l.append(random.randrange(1,10))
    L.append(l)

X = getMaxRect(L)
B = L
print "For Matrix L: " 
printMat(B)
print "%d is the largest area" % X
for i in areaDict.keys():
    if areaDict[i] == X:
        print "%d has the largest area with %d" % (i, X)        
