def doBFS(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

def printBFSPath(graph, start, goal):
	queue = [(start, [start])]
	# print queue
	while queue:
		# print queue
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				queue.extend([(next, path + [next])])


def doDFS(graph, start, visited = None):
	if visited is None:
		visited = set()

	visited.add(start)
	for next in graph[start] - visited:
		doDFS(graph, next, visited)
	return visited


def printDFSPath(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		vertex, path = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.extend([(next, path + [next])])
	return

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print "This is BFS Stuff"
print doBFS(graph, 'A')
print list(printBFSPath(graph, 'A','F'))
print list(printBFSPath(graph, 'A','X'))
print 
print "This is DFS Stuff"
print doDFS(graph, 'A')
print list(printDFSPath(graph, 'A', 'F'))
print list(printDFSPath(graph, 'A', 'X'))
print list(printDFSPath(graph, 'A', 'E'))