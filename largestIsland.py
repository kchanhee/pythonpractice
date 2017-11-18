def get_biggest_region(grid):
	biggest = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] != 1:
				continue
			elif grid[i][j] == 1:
				biggest = max(get_area(i,j, grid), biggest)
				# print "biggest area = %d" % biggest

	return biggest
    
def get_area(i, j, grid, area = 0):
	# print "(i, j) = (%d, %d)" % (i, j)
	# print "Current area: %d" % area
	# printGrid(grid)
	# print
	if i == len(grid):
		return
	if j == len(grid[i]):
		return
	if i < 0:
		return
	if j < 0:
		return
	if grid[i][j] == 0:
		return
	if grid[i][j] == 1:
		grid[i][j] = 'X'
		area += 1
		area = max(get_area(i + 1, j, grid, area), area)
		area = max(get_area(i, j + 1, grid, area), area)
		area = max(get_area(i + 1, j + 1, grid, area), area)
		area = max(get_area(i - 1, j, grid, area), area)
		area = max(get_area(i - 1, j - 1, grid, area), area)
		area = max(get_area(i, j - 1, grid, area), area)
		area = max(get_area(i + 1, j - 1, grid, area), area)
		area = max(get_area(i - 1, j + 1, grid, area), area)
	return area

	# return the sum of all adjacent cells
	


def printGrid(grid):
	for i in grid:
		print i


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
