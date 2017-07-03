r = int(raw_input().strip())
c = int(raw_input().strip())
grid = []
for rows in xrange(r):
    C = map(int, raw_input().strip().split(' '))
    grid.append(C)

# do flood fill
def getConnectedSize(grid, tup, visited):
    row, col = tup
    print "Currently on: (%d, %d) | visited: %d" % (row, col, len(visited))
    if row == len(grid) or col == len(grid[0]) or row < 0 or col < 0:
        return None
    if grid[row][col] == 1:
        visited.add(tup)
        grid[row][col] = 'X'
        getConnectedSize(grid, (row + 1, col), visited)
        getConnectedSize(grid, (row - 1, col), visited)
        getConnectedSize(grid, (row, col + 1), visited)
        getConnectedSize(grid, (row, col - 1), visited)
        getConnectedSize(grid, (row + 1, col - 1), visited)
        getConnectedSize(grid, (row + 1, col + 1), visited)
        getConnectedSize(grid, (row - 1, col + 1), visited)
        getConnectedSize(grid, (row - 1, col - 1), visited)
    elif tup in visited or grid[row][col] == 0:
        return None
    return visited
    


def printGrid(g):
    for r in g:
        print r

connected = []

for i in range(r):
    for j in range(c):

        if grid[i][j] == 1:
            visited = set()
            connected.append(len(getConnectedSize(grid,(i,j), visited)))
            printGrid(grid)
        else:
            continue
print connected
print max(connected)
