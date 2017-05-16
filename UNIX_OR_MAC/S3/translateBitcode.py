import sys
class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None

class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self, code, letter=None, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node()
        else:
            node = node
            while True:
                if code == 0:
                    # go left
                    if node.left == None:
                        node.left = tree
                        node.parent = node
                        if len(letter) == 1:
                            node.left.data = letter
                        break
                    node = node.left
                else:
                    # go right
                    if node.right == None:
                        node.right = tree
                        node.parent = node
                        if len(letter) == 1:
                            node.right.data = letter
                        break
                    node = node.right
        return tree

    def findLetter(self, code, node):
        if node is None:
            node = self.root
        while root is not None:
            if root.data is not None:
                return root.data
            if code[0] == 0:
                return root.findLetter(code[1:], root.left)
            else:
                return root.findLetter(code[1:], root.right)


def translateBitcode():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    codes = content[1:-2] 
    binary_code = content[-1]
    binary_tree = constructBinaryTree(codes)
    final_string = ""
    counter = 0
    while len(binary_code) > 0:
        if binary_tree.findLetter(binary_code[0:1 + counter]):
            final_tree += binary_code[0:1 + counter]
            del binary_code[0:1 + counter]
            counter = 0
        else:
            counter += 1
    return final_string


def constructBinaryTree(codes):
    tree = Tree()
    for line in codes:
        letter = line[0]
        code = line[2:]
        for bit in range(0, len(code)):
            if bit == len(code) - 1:
                tree.insert(bit,letter=letter)
            else:
                tree.insert(bit)
    return tree


