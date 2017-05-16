# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        if A is None or A.next is None:
            return A

        leftList = None
        head = None
        rightList = None
        rightListHead = None
        count = 0
        while A is not None and count < 10:
            if A.val >= B:
                if rightList is None:
                    print "RIGHT LIST INIT"
                    rightList = A
                    rightListHead = rightList
                else:
                    print "%d should go in right list. " % A.val
                    rightList.next = A
                    rightList = rightList.next
                    print rightList.val
            else:
                if leftList is None:
                    print "LEFT LIST INIT"
                    leftList = A
                    head = leftList
                else:
                    print "%d should go in left list. " % A.val
                    leftList.next = A
                    leftList = leftList.next
            A = A.next
            count += 1
        rightList.next = None
        printList(head)
        printList(rightListHead)
        if (head is None):
            return rightListHead

        leftList.next = rightListHead
        return head
        
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

A = createList([4,3,5,1,2,10])
B = createList([5,1,8,4,6,3,7,8,9])
C = createList([1,6,5,8,7,9,7,4,5,2,6,10])
D = createList([384, 183, 463, 31])

s = Solution()
# printList(s.partition(A, 3))
printList(s.partition(D, 77))
# s.partition(D, 77)
# s.partition(A, 3)

