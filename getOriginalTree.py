inOrderList = []
preOrderList = []
# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
    	return 'Node({})'.format(self.val)


# def inOrder(A):
# 	if A.left:
# 		inOrder(A.left)

# 	inOrderList.append(A.val)
# 	if A.right:
# 		inOrder(A.right)

def serialize(A):
	comp = []
	def preOrder(A, comp):
		comp.append(str(A.val))
		if A.left:
			comp.append('L')
			preOrder(A.left, comp)
		if A.right:
			comp.append('R')
			preOrder(A.right, comp)
		comp.append('U')
		return ''.join(comp)
	preOrder(A, comp)
	comp.pop()
	return ''.join(comp)


def getOriginal(A):
	# inOrder(A)
	string = serialize(A)
	print string
	L = []
	buff = ''
	for char in string:
		if char in ('L','R','U'):
			if buff:
				L.append(int(buff))
				buff = ''
			L.append(char)
		else:
			buff += char
	L.reverse()
	print L
	nodes = [Node(L.pop())] # root node

	def rebuild():
		val = L.pop()
		if val == 'L':
			nodes[-1].left = Node(L.pop())
			nodes.append(nodes[-1].left)
		if val == 'R':
			nodes[-1].right = Node(L.pop())
			nodes.append(nodes[-1].right)
		if val == 'U':
			nodes.pop()
		if L:
			rebuild()
	rebuild()
	return nodes[0]

x = Node(4)
x.left = Node(3)
x.left.left = Node(2)
x.right = Node(5)
x.right.left = Node(8)
x.right.right = Node(7)
