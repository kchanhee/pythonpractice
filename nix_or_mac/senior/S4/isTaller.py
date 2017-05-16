def isTaller(p, q, height_dict):
    if p not in height_dict.keys():
        return False
    visited, queue = set(), list(height_dict[p])
    while queue:
        vertex = queue.pop(0)
        # print vertex
        if vertex == q:
            return True
        if vertex not in visited:
            visited.add(vertex)
            if vertex in height_dict:
                queue.extend(list(height_dict[vertex] - visited))
            else:
                continue    
            
    return False

def makeHeightDict(edge_pairs):
    height_dict = {}
    for pers1, pers2 in edge_pairs:
        if pers1 in height_dict:
            height_dict[pers1].add(pers2)
        else:
            height_dict[pers1] = set([pers2])
    return height_dict

for i in range(6):
    for j in range(5):
        infile = open("s4." + str(i+1) + "-" + str(j+1) +  ".in", "r")
        outfile = open("s4." + str(i+1) + "-" + str(j+1) + ".out", "r")
 
        n = infile.readline().rstrip().split()

        num_stud, num_cmps = int(n[0]), int(n[1])
        # print num_stud, num_cmps
        # break
        edge_pairs = []
        for k in range(num_cmps):
            line = infile.readline().rstrip().split()
            edge_pairs.append((line[0], line[1]))
        height_dict = makeHeightDict(edge_pairs)

        # preprocess
        while True:
            line = infile.readline().rstrip().split()
            answer = outfile.readline().strip()
            if len(line) == 0:
                break
            p, q = line[0],line[1]
            p_q = isTaller(p, q, height_dict)
            q_p = isTaller(q, p, height_dict)
            if p_q:
                result = 'yes'
            elif q_p:
                result = 'no'
            else:
                result = 'unknown'
            # print result, answer, 'file: s4.%d-%d:' % (i+1,j+1)
            print (result == answer)
            # print
        infile.close()
        outfile.close()