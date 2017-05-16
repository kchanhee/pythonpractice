import sys
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insert(self, bitcode, letter):
        if len(bitcode) == 0:
            self.data = letter
            return
        where = bitcode[0]
        bitcode = bitcode[1:]
        if where == "0":
            if self.left == None:
                self.left = Tree()
            self.left.insert(bitcode, letter)
        else:
            if self.right == None:
                self.right = Tree()
            self.right.insert(bitcode, letter)

    def traverse(self, bitcode):
        if bitcode == "0":
            return self.left
        else:
            return self.right


def translateBitcode(binary_code, pairs):
    binary_tree = Tree()
    curr_node = binary_tree
    for char, bitcode in pairs:
        binary_tree.insert(bitcode, char)
    final_string = ""
    for bit in binary_code:
        curr_node = curr_node.traverse(bit)
        if curr_node.data != None:
            final_string += curr_node.data
            curr_node = binary_tree
    return final_string


def constructBinaryTree(codes):
    tree = Tree()
    for line in codes:
        letter = line[0]
        code = line[2:]
        tree.insert(code, letter)
    return tree


for i in range(6):
    infile = open("s2." + str(i+1) + ".in", "r")
    outfile = open("s2." + str(i+1) + ".out", "r")
    answer = outfile.readline().rstrip()
    h = int(infile.readline().rstrip())
    pairs = []
    for i in range(h):
        line = infile.readline().rstrip().split(" ")
        pairs.append((line[0], line[1]))
    encoded_str = infile.readline().rstrip()
    result = translateBitcode(encoded_str, pairs)
    print(i + 1, result==answer)
    infile.close()
    outfile.close()

