# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        count = 1
        start = None
        final = None
        head = A
        start_copy = head
        while count <= n:
            if m != 1 and count == m - 1:
                start_copy = A
            if count == m:
                start = A
            elif count == n:
                final = A.next
                A.next = None
                h, t = reverse(start)
                t.next = final
                if m == 1:
                    return h
                else:
                    start_copy.next = h
            A = A.next
            count += 1
        return head


# Function to reverse the linked list
def reverse(A):
    prev = None
    current = A
    tail = A
    while(current is not None):
        # print current.val
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev, tail # this returns the head and tail of reversed matrix

def createList(arr):

    A = ListNode(arr[0])
    head = A
    for i in range(1, len(arr)):
        A.next = ListNode(arr[i])
        A = A.next
    return head

def printList(A):
    while (A is not None):
        print A.val, " -> ",
        A = A.next
    print
A = createList([1,2,3,4,5])
B = createList([1,2,3,4,5,6,7,8,9])
C = createList([1,2,3])
s = Solution()
# s.reverseBetween(A, 2, 4)
# printList(s.reverseBetween(A, 2, 5))
# printList(s.reverseBetween(B, 6, 8))
printList(s.reverseBetween(C, 1, 2))
# printList(reverse(A))

