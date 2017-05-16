# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        root = A
        if root == None:
            return 0
        # tree: {node.val : [node.left.val, node.right.val]}
        s = 0
        ans = 0
        stack = [[root, 0]]

        while stack: # depth first search
            node, num = stack.pop()
            num = num * 10 + node.val
            if node.left:
                stack.append([node.left, num])
            if node.right:
                stack.append([node.right, num])
            if not node.left and not node.right:
                s += num
        return s % 1003
        