

for i in range(1,10):
    infile = open("s5." + str(i+1) + ".in", "r")
    outfile = open("s5." + str(i+1) + ".out", "r")
 
    n = int(infile.readline().rstrip())
    lights = []
    for j in range(n):
        line = infile.readline().rstrip().split()

        lights.append(int(line[0]))
    print lights
    answer = outfile.readline().rstrip()
    print int(answer)
    # print(result == answer)
 
    infile.close()
    outfile.close()