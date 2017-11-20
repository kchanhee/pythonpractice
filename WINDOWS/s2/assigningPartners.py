
def checkPartners(pairs):
    if len(pairs.keys()) % 2 != 0:
        return "bad"
    for i in pairs.keys():
        partner = pairs[i]
        if pairs[partner] != i:
            return "bad"
        if pairs[partner] == partner:
            return "bad"
    return "good"

for i in range(5):
    infile_a = open("s2." + str(i+1) + "a.in", "r")
    infile_b = open("s2." + str(i+1) + "b.in", "r")
    outfile_a = open("s2." + str(i+1) + "a.out", "r") 
    outfile_b = open("s2." + str(i+1) + "b.out", "r") 

    N_a = int(infile_a.readline().rstrip())
    N_b = int(infile_b.readline().rstrip())


    row1_a = infile_a.readline().rstrip().split(' ')
    row2_a = infile_a.readline().rstrip().split(' ')
    pairs_a = {}

    for j in range(N_a):
        pairs_a[row1_a[j]] = row2_a[j]


    row1_b = infile_b.readline().rstrip().split(' ')
    row2_b = infile_b.readline().rstrip().split(' ')
    pairs_b = {}

    for k in range(N_b):
        pairs_b[row1_b[k]] = row2_b[k]


    ans_a = outfile_a.readline().rstrip()
    ans_b = outfile_b.readline().rstrip()
    my_ans_a = checkPartners(pairs_a)
    my_ans_b = checkPartners(pairs_b)

    print "Answer to A - %d: %s" % (i + 1, ans_a)
    print "My answer:   %s" % my_ans_a
    print
    print ans_a == my_ans_a
    print

    print "Answer to B - %d: %s" % (i + 1, ans_b)
    print "My answer:   %s" % my_ans_b
    print
    print ans_b == my_ans_b
    print

