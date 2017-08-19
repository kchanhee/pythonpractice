#!/bin/python

import sys
def doDFS(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,x,y = raw_input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    graph = {}
    
    for a1 in xrange(m):
        city_1,city_2 = raw_input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        if city_1 in graph.keys() and city_2 in graph.keys():
            graph[city_1].add(city_2)
            graph[city_2].add(city_1)
        elif city_1 in graph.keys():
            graph[city_1].add(city_2)
            graph[city_2] = set([city_1])
        elif city_2 in graph.keys():
            graph[city_1] = set([city_2])
            graph[city_2].add(city_1)
        else:
            graph[city_1] = set([city_2])
            graph[city_2] = set([city_1])
    keys = set(graph.keys())
    lib_count = 0
    road_count = 0
    # library cost is cheaper than building roads, just build library at every city
    if x < y: 
        print len(keys) * x
        continue
    while keys:
        start = keys.pop()
        curr_roads = doDFS(graph, start)
        keys -= curr_roads
        road_count += len(curr_roads) - 1
        lib_count += 1
        # print curr_roads
    print min(lib_count * x + road_count * y, len(graph.keys()) * x)



# print doDFS(graph, 1)
