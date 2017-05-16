import sys
# @param G: Graph {V1:[(E1,D1),(E2,D2),..], V2:}
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
    }


# def dijkstra(nodes, distances, root, end):
#     unvisited = {node: None for node in nodes}
#     visited = {}
#     current = root
#     currentDist = 0
    
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # all nodes have max dist until they're visited
        self.distance = sys.maxint
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_id(self):
        return self.id

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent:' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, curr, next, cost = 0):
        if curr not in self.vert_dict:
            self.add_vertex(curr)
        if next not in self.vert_dict:
            self.add_vertex(next)
        self.vert_dict[curr].add_neighbor(self.vert_dict[next], cost)
        self.vert_dict[next].add_neighbor(self.vert_dict[curr], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous '''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    start.set_distance(0)
    unvisited = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited)
    while len(unvisited):
        # Pop vertex with smallest distance
        uv = heapq.heappop(unvisited)
        curr = uv[1]
        curr.set_visited()

        for next in curr.adjacent:
            if next.visited:
                continue
            new_distance = curr.get_distance() + curr.get_weight(next)

            if new_distance < next.get_distance():
                next.set_distance(new_distance)
                next.set_previous(curr)
            
        # rebuild heap
        # 1. Pop every item
        while len(unvisited):
            heapq.heappop(unvisited)
        # 2. put all vertices not visited into the queue
        unvisited = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited)



g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)  
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print 'Graph data:'
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

dijkstra(g, g.get_vertex('a'), g.get_vertex('e')) 

target = g.get_vertex('e')
path = [target.get_id()]
shortest(target, path)
print 'The shortest path : %s' %(path[::-1])


