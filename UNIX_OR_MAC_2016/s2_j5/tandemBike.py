
def totalSpeed(q_type, D_speeds, P_speeds):
    if q_type == 1:
        total = 0
        for i in range(len(D_speeds) - 1, -1, -1):
            total += max(D_speeds[i], P_speeds[i])
        return total
    else:
        tot_1 = 0
        tot_2 = 0 
        for i in range(len(D_speeds)):
            tot_1 += max(D_speeds[i], P_speeds[-i - 1])
            tot_2 += max(D_speeds[-i - 1], P_speeds[i])
        return max(tot_1, tot_2)

for i in range(18):
    infile = open("s2." + str(i+1) + ".in","r")
    outfile = open("s2." + str(i+1) + ".out","r")
    q_type = int(infile.readline().rstrip())
    N = int(infile.readline().rstrip())
    D_speeds = map(int, infile.readline().rstrip().split(' '))
    D_speeds = sorted(D_speeds)
    P_speeds = map(int, infile.readline().rstrip().split(' '))
    P_speeds = sorted(P_speeds)

    answer = int(outfile.readline().rstrip())

    print totalSpeed(q_type,D_speeds, P_speeds) == answer



    