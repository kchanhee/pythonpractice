# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A is None:
            return None
        slowNode = A
        fastNode = A
        while (slowNode and fastNode and fastNode.next):
            slowNode = slowNode.next
            fastNode = fastNode.next.next
            if (slowNode == fastNode):
                # There is a cycle:
                slowNode = A
                while slowNode.val != fastNode.val:
                    slowNode = slowNode.next
                    fastNode = fastNode.next
                return slowNode
            
        return None