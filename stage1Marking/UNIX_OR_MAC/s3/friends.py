class ListNode:
    def __init__(self, name, count=0):
        self.name = name
        self.next = None

def isFriends(friend1, friend2, friendDict):
    seen_friend = {}
    current_friend = friendDict[friend1]
    connected = False
    circular = False
    sep_count = 0
    while current_friend not in seen_friend:
        if current_friend == friend2:
            connected = True
        elif current_friend == friend1:
            circular = True
        seen_friend[current_friend] = friendDict[current_friend]
        current_friend = friendDict[current_friend]
        if not connected:
            sep_count += 1
    if connected and circular:
        return "Yes %d" % sep_count
    return "No"
        

def constructLink(edge_pairs):
    friendDict = {}
    for frnd_a, frnd_b in edge_pairs:
        friendDict[frnd_a] = frnd_b
    return friendDict
 
for i in range(4):
    infile = open("s3." + str(i+1) + ".in", "r")
    outfile = open("s3." + str(i+1) + ".exp", "r")
 
    n = int(infile.readline().rstrip())
    edge_pairs = []
    for j in range(n):
        line = infile.readline().rstrip().split()
        edge_pairs.append((line[0], line[1]))
    friends_dict = constructLink(edge_pairs)
    # print friends_dict
    while True:
        line = infile.readline().rstrip()
        if line == "0 0":
            break
        line = line.split()
        frnda, frndb = line

        # result = degree_of_sep(frnda, frndb, adjdict)
        result = isFriends(friends_dict[frnda], friends_dict[frndb], friends_dict)
        answer = outfile.readline().rstrip()
        # print result, answer
        print(result == answer)
 
    infile.close()
    outfile.close()

