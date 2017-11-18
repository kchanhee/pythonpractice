import sys


def removeFriends(friends, round_vals):
	if len(round_vals) == 0:
		# print friends
		return friends
	new_friends = []
	for i in range(1, len(friends) + 1):
		if i % round_vals[0] != 0:
			new_friends.append(friends[i - 1])
	return removeFriends(new_friends, round_vals[1:])


# if __name__ == "__main__":
# 	friends = int(raw_input().strip())
# 	rounds = int(raw_input().strip())
# 	round_vals = []
# 	for a0 in xrange(rounds):
# 		n = int(raw_input().strip())
# 		round_vals.append(n)
# 	friend_arr = range(1, friends + 1)
# 	removeFriends(friend_arr, round_vals)

for i in range(5):
	infile = open("s1." + str(i+1) + ".in","r")
	outfile = open("s1." + str(i+1) + ".out","r")
	friends = int(infile.readline().rstrip())
	rounds = int(infile.readline().rstrip())
	round_vals = []
	for a0 in xrange(rounds):
		n = int(infile.readline().rstrip())
		round_vals.append(n)

	friend_arr = range(1, friends + 1)
	# print friend_arr
	# print round_vals
	new_friends = removeFriends(friend_arr, round_vals)
	# print new_friends
	j = 0
	while True:
		answer = outfile.readline().rstrip()
		print answer
		if len(answer) == 0 and j < len(new_friends):
			print "Not quite right 1"
			break
		if len(answer) != 0 and j == len(new_friends):
			print "Not quite right 2"
			break			
		if len(answer) == 0 or j == len(new_friends):
			break
		print "friend : %d | %d : answer" % (new_friends[j], int(answer))
		print new_friends[j] == int(answer)
		j += 1
