def Sudoku(file):
	A = []
	with open(file) as f:
		line = f.readline()
		# print line
		while line != "":
			# print line
			results = map(int,line.split())
			A.append(results)
			line = f.readline()
	# for i in A:
	# 	print i
	S = completeBoard(A)
	# return A
	if (S):
		for i in A:
			print i
	else:
		return "NO SOLUTION"
	# return A


def completeBoard(A):
	(r,c) = findUnassignedLocation(A)
	# print (r,c)
	if r < 0 or c < 0:
		return True # board is complete
	for N in range(1, 10):
		if checkNumberValid(N, r, c, A):
			A[r][c] = N
			if completeBoard(A):
				return True
			A[r][c] = 0
	return False

def findUnassignedLocation(A):
	for r in range(len(A)):
		for c in range(len(A[r])):
			if A[r][c] == 0:
				return (r, c)
	return (-1,-1) # this means no more unassigned spots

def checkNumberValid(N, r, c, A):
	return checkNumberValidRow(N, r, A) and checkNumberValidCol(N, c, A) and checkSubCellValid(N, r, c, A)

def checkNumberValidRow(N, r, A):
	if N in A[r]:
		return False
	return True

def checkNumberValidCol(N, c, A):
	for i in range(9):
		if A[i][c] == N:
			return False
	return True

def checkSubCellValid(N, r, c, A):
	s_r = r - r % 3
	s_c = c - c % 3
	for i in range(s_r, s_r + 3):
		for j in range(s_c, s_c + 3):
			if A[i][j] == N:
				return False
	return True

# Sudoku('2.sd')
for i in range(1, 10):
	print '%d.sd' % i
	Sudoku('%d.sd' % i)