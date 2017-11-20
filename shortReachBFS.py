
#!/bin/python

import sys



def getDistances(graph, start):
    distances = {start : 0}
    queue = [start]
    # print graph
    while queue:
        element = queue.pop(0)
        # print element
        if element in graph:
            distance = distances[element] + 6
            for neighbor in graph[element]:
                if (neighbor in distances): 
                    continue
                distances[neighbor] = distance
            queue.append(neighbor)
    return distances

def getShortestPath(N, graph, start):
    distances = getDistances(graph, start)
    # print distances
    pathList = []
    # print distances
    for i in range(1, N + 1):
        # print i
        if i == start:
            # print "start node"
            continue
        if i in distances:
            # print "distance from %d to %d: %d"  % (start, i, distances[i])
            pathList.append(distances[i])
            # print pathList
        else:
            # print "not in path. "
            pathList.append(-1)
    return pathList

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, m = raw_input().strip().split(' ')
        n, m = [int(n), int(m)]
        graph = {}

        for a1 in xrange(m):
            u, v = raw_input().strip().split(' ')
            u, v = [int(u), int(v)]
            if u in graph: 
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        # print
        s = int(raw_input().strip())
        pathList = getShortestPath(n, graph, s)
        # print pathList
        for j in pathList:
            print j, 
        print

        