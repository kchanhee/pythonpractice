'''Problem: Given input m x n matrix, find the total number of unique islands,
where an island is defined as horizontally and vertically adjacent cells of ones'''

def findUniqueIslands(mat):
	num_rows = len(mat)
	num_cols = len(mat[0])
	lookup_table = []
	for i in range(num_rows):
		lookup_table.append([0]*num_cols)

	i, j = 0, 0
	num_islands = 0
	for i in range(num_rows):
		for j in range(num_cols):
			# print "current coord: %d, %d | val: %d, lookup: %d" % (i,j, mat[i][j], lookup_table[i][j])
			if mat[i][j] == 1 and lookup_table[i][j] == 0:
				num_islands += 1
				doBFS(mat, i, j, lookup_table)
		
	# print lookup_table[2][0]




	return num_islands

def doBFS(mat, row, col, lookup_table):
	if row < 0 or row == len(mat):
		return
	if col < 0 or col == len(mat[row]):
		return
	# print "curr pt: %d, %d" % (row,col) 
	i,j= row,col
	print "current coord: %d, %d | val: %d, lookup: %d" % (i,j, mat[i][j], lookup_table[i][j])

	if mat[row][col] == 1 and lookup_table[row][col] == 0:
		lookup_table[row][col] = 1
		doBFS(mat, row, col + 1, lookup_table)
		doBFS(mat, row, col - 1, lookup_table)
		doBFS(mat, row + 1, col, lookup_table)
		


mat = [ [0,1,1],
		[0,1,1],
		[1,0,0]]

mat2 = [[1]*5,
		[0]*2+[1]*3,
		[1]+[0]*4]

# print mat2
# print findUniqueIslands(mat)
print findUniqueIslands(mat2)