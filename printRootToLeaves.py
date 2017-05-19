'''
Q1:

     ABC
     /\
    D  E
   /|\  \
  F G H  I
 
goal: print all paths from root to leaves.

ABCDF
ABCDG
ABCDH
ABCEI

'''

class Node:
	def __init__(self,data):
		self.data = data
		self.children = []

def getAllPaths(root, start, curr_text=""):
	curr_text += start.data
	# iterate through children and pass down text
	for c in start.children:
		getAllPaths(root, c, curr_text)
	# print when at leaf
	if len(start.children) == 0:
		print curr_text



node1 = Node("ABC")
node1.children =[Node("D"), Node("E")]
node1.children[0].children = [Node("F"), Node("G"), Node("H")]
node1.children[1].children = [Node("I")]

getAllPaths(node1,node1)
# print getAllPaths
# print len(visited)
# print printAllPaths(visited)
# print printAllPaths(visited)