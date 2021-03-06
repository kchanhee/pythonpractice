'''You are given a list of words like
["d", "a", "aa", "b", "bbc", "aab", "aac", "baac"]
your objective is to find the length of the longest sequence of words in the 
list so that each word is only one character away from the other

so for this test example, the answer is "a", "aa", "aac", "baac" so you should return 4'''

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.children = []

# def maxDepth(node):
# 	if node is None:
# 		return 0
# 	else:
# 		childDepths = []
# 		for c in node.children:
# 			childDepths.append(maxDepth(c))
		
# 	if len(childDepths) == 0:
# 		return 1
# 	return max(childDepths) + 1

# def buildTree(word, word_set, visited_words):
# 	if len(word) == 0 and word in visited_words:
# 		return None

# 	n = Node(word)
# 	for i in range(0, len(word)):
# 		sub_word = word[0:i] + word[i+1:]
# 		if sub_word in word_set and sub_word not in visited_words:
# 			n.children.append(buildTree(sub_word, word_set, visited_words))
	
# 	return n

# def longestSequence(word_list):
# 	# max_word_len = len(word_list[-1])
# 	word_set = set(word_list)
# 	visited_words = set()
# 	trees = []
# 	for i in range(len(word_list) - 1, -1, -1):
# 		trees.append(buildTree(word_list[i], word_set, visited_words))
# 		visited_words.add(word_list[i])
# 	max_length = 0
# 	for root in trees:
# 		if len(data) <= max_length:
# 			continue
# 		maxRootDepth = maxDepth(root)
# 		if maxRootDepth > max_length:
# 			max_length = maxRootDepth

# 	return max_length 
# Use recursion to find the maximum depth of each word. The depth_dict is updated as the deepest subword is reached.
def maxDepth(word, word_set, depth_dict):
    depth_dict[word] = 1
    for i in range(len(word)):
        sub_word = word[0:i] + word[i+1:]
        if sub_word in word_set:
            if sub_word not in depth_dict: # need to go and see how deep down the word_set the sub_word goes.
                maxDepth(sub_word, word_set, depth_dict)
            # get the max depth for the current word.
            depth_dict[word] = max(depth_dict[word], depth_dict[sub_word] + 1)
    
def longestSequence(words):
    word_set = set(words) # sets are O(1) lookup
    max_depth = 0
    # dictionary to keep track of each word's maximum depth
    depth_dict = {}
    for w in word_set:
        maxDepth(w, word_set, depth_dict)
    return max(depth_dict.values())

A = ["d", "a", "aa", "b", "bbc", "aab", "aac", "baac"]
B = ["d", "a", "aa", "b", "bbc", "aab", "aac", "baac", "baace"]
C = ["a", "ab", "ca", "de"]
D = ["a", "cc", "ac", "abd", "acd", "ace", "aced", "acedf", "gacedf"]
E = ["a", "c", "b"]

print longestSequence(A) == 4
print longestSequence(B) == 5
print longestSequence(C) == 2
print longestSequence(D) == 6
print longestSequence(E) == 1
