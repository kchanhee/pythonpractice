# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        root = A
        curr_lvl = [A]
        left = True # start with left and switch when the end is hit
        lvl = 0 # top level is 0, which means the ith list in the list can only have up to 2^lvl elements
        L = [[root.val]]
        while curr_lvl:
            left = not left
            next_lvl = list()
            next_lvl_vals = list()
            # nextLvl = getList(curr_lvl, left)
            for n in curr_lvl:
                # if left:
                if n.left: 
                    next_lvl.append(n.left)
                    next_lvl_vals.append(n.left.val)
                if n.right: 
                    next_lvl.append(n.right)
                    next_lvl_vals.append(n.right.val)
                # # else:
                #     if n.right: 
                #         next_lvl.append(n.right)
                #         next_lvl_vals.append(n.right.val)
                #     if n.left: 
                #         next_lvl.append(n.left)
                #         next_lvl_vals.append(n.left.val)
            curr_lvl = next_lvl
            if len(next_lvl_vals) > 0:
                if left:
                    L.append(next_lvl_vals)
                else:
                    L.append(list(reversed(next_lvl_vals)))
        return L


