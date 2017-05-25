def getPathBFS(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in graph.keys():
            return -1
        for next in graph[vertex] - set(path):
            if next == end:
                return 6 * (len(path))
            else:
                queue.append((next, path + [next]))
    return -1

q = int(raw_input().strip())
for a0 in xrange(q):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n), int(m)]
    adj_dict = {}
    for i in xrange(m):
        a,b = map(int, raw_input().split())
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
    start = map(int, raw_input().split())[0]
    
    all_nodes = range(1,n + 1)
    for i in all_nodes:
        if start == i:
            continue
        # print "(start, end): (%d, %d)" % (start, i)
        if i not in adj_dict:
            print -1,
            continue
        path_len = getPathBFS(adj_dict, start, i)
        print path_len,
        
             
    print 