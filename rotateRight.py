# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        nodes = []
        while A:
            nodes.append(A)
            A = A.next
        length = len(nodes)
        
        true_rotate = B % length # 'tis a circle so rotating multiple times is pointless :)
        if true_rotate == 0: # this is a complete cycle, no need to even rotate
            return nodes[0]
        if length == 1:
            return nodes[0]
        if length == 2:
            nodes[1].next = nodes[0]
            nodes[0].next = None
            return nodes[1]
        if length > 3:
            # this is to represent n-1th element since arr idx start at 0
            # this is the node at the end now
            # print true_rotate
            nodes[-true_rotate-1].next = None
            nodes[-1].next = nodes[0]

        return nodes[-true_rotate] # return the new head node. 


def createList(arr):

    A = ListNode(arr[0])
    head = A
    for i in range(1, len(arr)):
        A.next = ListNode(arr[i])
        A = A.next
    return head

def printList(A):
    while (A is not None):
        if A.next is None:
            print A.val
            break
        print A.val, " -> ",
        A = A.next
    print

A = createList([1,2,3,4,5])
B = createList([1,2,3,4,5,6,7,8,9])
C = createList([1,2,3])

s = Solution()

printList(s.rotateRight(A, 3))
printList(s.rotateRight(B, 4))
# s.rotateRight(A, 5)
# s.rotateRight(A, 2)
# s.rotateRight(A, 1)