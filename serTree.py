# Given a Binary Tree with integers as values, write code to 
# 1) Serialize the Binary Tree into a list of integers - 
#   List<int> store (Node root)
# 2) Use the list generated in 2 to deserialize and obtain the original Binary tree
#   Node restore(List<int> list)
#         4       
#    3          5
# 2    null   8   7

# In order List (L->P->R)
# [2, 3, 4, 8, 5, 7]
# Pre order
# [4, 3, 2, 5, 8, 7]
# Post Order
# [2, 3, 4, 8, 7, 5]

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({})'.format(self.val)

BT = Node(4)
BT.left = Node(3)
BT.left.left = Node(2)
BT.right = Node(5)
BT.right.left = Node(8)
BT.right.right = Node(7)


def serialize_bt(bt):
    components = []

    def incorporate(bt, components):
        components.append(str(bt.val))
        if bt.left:
            components.append('L')
            incorporate(bt.left, components)
        if bt.right:
            components.append('R')
            incorporate(bt.right, components)
        components.append('U')
        return ''.join(components)

    incorporate(bt, components)
    components.pop()
    return ''.join(components)


def deserialize(string):
    chars = ''
    nodes = []
    next_child = None
    for i, char in enumerate(string):
        if char not in ('L', 'R', 'U'):
            chars += char
        else:
            if not nodes:
                nodes.append(Node(int(chars)))
            elif next_child == 'left':
                nodes[-1].left = Node(int(chars))
                nodes.append(nodes[-1].left)
            elif next_child == 'right':
                nodes[-1].right = Node(int(chars))
                nodes.append(nodes[-1].right)
            elif next_child == 'up':
                nodes.pop()
            if char == 'L':
                next_child = 'left'
            elif char == 'R':
                next_child = 'right'
            elif char == 'U':
                next_child = 'up'
            chars = ''
    return nodes[0]


def deserialize_recursive(string):
    list_ = []
    chars = ''
    print string
    for char in string:
        if char in ('L', 'R', 'U'):
            if chars:
                list_.append(int(chars))
                chars = ''
            list_.append(char)
        else:
            chars += char
    list_.reverse()
    print list_

    nodes = [Node(list_.pop())]  # The root node

    def rebuild():
        val = list_.pop()
        if val == 'L':
            nodes[-1].left = Node(list_.pop())
            nodes.append(nodes[-1].left)
        if val == 'R':
            nodes[-1].right = Node(list_.pop())
            nodes.append(nodes[-1].right)
        if val == 'U':
            nodes.pop()
        if list_:
            rebuild()

    rebuild()
    return nodes[0]