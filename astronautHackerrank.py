
def doDFS(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

import operator as op
def ncr(n, r):
    if n < r: return 0
    r = min(r, n-r)
    
    if r == 0: return 1
    
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())

adj_dict = {}
for i in xrange(l):
    a,b = map(int,raw_input().split())
    if a in adj_dict.keys() and b in adj_dict.keys():
    # Store a and b in an appropriate data structure
        adj_dict[a].add(b)
        adj_dict[b].add(a)
    elif a in adj_dict.keys():
        adj_dict[a].add(b)
        adj_dict[b] = set([a])
    elif b in adj_dict.keys():
        adj_dict[a] = set([b])
        adj_dict[b].add(a)
    else:
        adj_dict[a] = set([b])
        adj_dict[b] = set([a])
ast_set = set(range(N))
keys = set(adj_dict.keys())
buckets = []
while keys:
    start = keys.pop()
    same_country = doDFS(adj_dict, start)
    buckets.append((same_country, len(same_country)))
    keys -= same_country
result = 0

for i in range(len(buckets)):
    N -= buckets[i][1]
    result += buckets[i][1] * N

print N
result += ncr(N,2)
print result
