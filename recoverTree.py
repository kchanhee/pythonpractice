# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.prev = None
        self.p1 = None
        self.p2 = None
        self.traverse(A)
        return [self.p2.val, self.p1.val]        

    
    # @param node: node in BST
    # @return list of integers if BST violation, None otherwise
    def checkNode(self, node):
        if node.left:
            if node.left.val > node.val:
                return [node.val, node.left.val]
        if node.right:
            if node.right.val < node.val:
                return [node.val, node.right.val]
        return []

    def traverse(self, root):
        if root.left:
            self.traverse(root.left)
        if self.prev is not None:
            if root.val < self.prev.val:
                self.p2 = root
                if self.p1 is None:
                    self.p1 = self.prev
        self.prev = root
        if root.right:
            self.traverse(root.right)