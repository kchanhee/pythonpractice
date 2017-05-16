# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        link_buffer = deque(maxlen = B + 1)
        list_length = 0
        head = A
        while A is not None:
            list_length += 1
            link_buffer.append(A)
            A = A.next
        if B >= list_length:
            # print list_length
            return head.next
        if B >= 2:
            left = link_buffer.popleft()
            link_buffer.popleft()
            left.next = link_buffer.popleft()    
        else:
            left = link_buffer.popleft()
            left.next = None

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
printList(s.removeNthFromEnd(A, 1))
printList(s.removeNthFromEnd(A, 10))
printList(s.removeNthFromEnd(B, 9))
printList(s.removeNthFromEnd(C, 4))
# s.partition(D, 77)