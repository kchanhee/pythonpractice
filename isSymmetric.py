# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        root = A
        curr_lvl = [A]
        this_level = 0
        while curr_lvl:
            l_count = 0 # of left children at the current lvl
            r_count = 0 # of right children at current lvl
            next_lvl = list()
            next_lvl_vals = list()
            # iterate through the nodes in the current_lvl
            # and count the number of leftchildren and rightchildren
            for n in curr_lvl:
                if n.left:
                    next_lvl.append(n.left)
                    next_lvl_vals.append(n.left.val)
                    l_count += 1
                if n.right: 
                    next_lvl.append(n.right)
                    next_lvl_vals.append(n.right.val)
                    r_count += 1
            # print "Level: " + str(this_level)
            # print "Children Values" + str(next_lvl_vals)
            # symmetry checks
            if len(next_lvl_vals) % 2 != 0:
                return 0
            # if the # of left_children != right_children, tree cannot be symmetric
            elif l_count != r_count:
                return 0
            # split the value array in half and compare if symmetric
            else:
                mid = len(next_lvl_vals) / 2
                if next_lvl_vals[:mid] != list(reversed(next_lvl_vals[mid:])):
                    return 0
            curr_lvl = next_lvl
            this_level += 1
        return 1