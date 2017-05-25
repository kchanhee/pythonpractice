#!/bin/python

import sys
from Queue import PriorityQueue

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = {}
    self.weights = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, weight):
    if from_node not in self.edges.keys():
        self.edges[from_node] = [to_node]
    if to_node not in self.edges.keys():
        self.edges[to_node] = [from_node]
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    if (from_node, to_node) not in self.weights and (to_node, from_node) not in self.weights:
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
    elif (from_node, to_node) not in self.weights:
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = min(weight, self.weights[(to_node, from_node)])
    elif (to_node, from_node) not in self.weights:
        self.weights[(from_node, to_node)] = min(weight, self.weights[(from_node, to_node)])
        self.weights[(to_node, from_node)] = weight
    else:
        self.weights[(from_node, to_node)] = min(weight, self.weights[(from_node, to_node)])
        self.weights[(to_node, from_node)] = min(weight, self.weights[(to_node, from_node)])

def doDijkstra(graph, start):
    visited = {start: 0}
    # path = {}
    nodes = graph.nodes
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node == None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        curr_weight = visited[min_node]
        for edge in graph.edges[min_node]:
            weight = curr_weight + graph.weights[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                # path[edge] = min_node

    return visited

t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = map(int,raw_input().split())
    # n,m = [int(n),int(m)]
    graph = Graph()
    for a1 in xrange(m):
        x,y,r = map(int,raw_input().split())
        # x,y,r = [int(x),int(y),int(r)]
        graph.add_node(x)
        graph.add_node(y)
        graph.add_edge(x,y,r)


    s = int(raw_input().strip())
    visited = doDijkstra(graph, s)

    for i in range(1,n+1):
        if i == s:
            continue
        if i not in visited:
            print -1,
            continue
        print visited[i],
    print