# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
     def maxPathSum(self, root):
        maxx = [float('-inf')]
        def mp(root):
            if not root:
                return 0
            mp_left = mp(root.left)
            mp_right = mp(root.right)
            curr = max(root.val, root.val+max(mp_left, mp_right))
            maxx[0] = max(maxx[0], max(curr, mp_left+mp_right+root.val))
            return curr
        mp(root)
        return maxx[0]
        
# tree = TreeNode(9)
tree = TreeNode(-100)
tree.left = TreeNode(-200)
tree.left.left = TreeNode(-300)
tree.left.left.left = TreeNode(-400)

# tree.left.left.right = TreeNode(5)
# tree.right.left = TreeNode(21)
# tree.right.right = TreeNode(30)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(4)

s = Solution()
print s.maxPathSum(tree)
print s.maxPathSum(tree2)

