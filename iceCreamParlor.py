def doSearch(C_sorted, m):
    lo = 0
    hi = len(C_sorted) - 1
    while lo < hi:
        if C_sorted[lo] + C_sorted[hi] == m:
            return (C_sorted[lo], C_sorted[hi])
        elif C_sorted[lo] + C_sorted[hi] < m:
            lo += 1
        else:
            hi -= 1
    return (None, None) # should never go here.

def printList(l):
    for tup in l:
        if tup[0] < tup[1]:
            print tup[0], tup[1]
        else:
            print tup[1], tup[0]


t = int(raw_input().strip())
l = []
for a in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    C = list(map(int,raw_input().strip().split(' ')))
    # print 
    # print "----- hello ----- "
    idx_dict = {}
    for i, v in enumerate(C):
        if v in idx_dict:
            idx_dict[v].append(i + 1)
        else:
            idx_dict[v] = [i + 1]
    C_sorted = sorted(C)
    i,j = doSearch(C_sorted, m)
    # l.append((i,j))
    # print i, j

    if (i == j):
        l.append((idx_dict[i][0], idx_dict[i][1]))
    else:
        l.append((idx_dict[i][0], idx_dict[j][0]))
printList(l)