# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        linkSum = ListNode(0)
        head = linkSum
        carry = 0
        count = 0
        while A is not None or B is not None or carry == 1:
            currSum = 0
            if A is not None and B is not None:
                currSum = A.val + B.val + carry
                A = A.next
                B = B.next
            elif A is not None:
                currSum = A.val + carry
                A = A.next
            elif B is not None:
                currSum = B.val + carry
                B = B.next
            else: # both nodes are exhausted but there's still a carry value to be added
                # print carry
                linkSum.next = ListNode(carry)
                linkSum.val = 0
                carry = 0
                break
            # print "current sum is: %d" % currSum
            count += 1
            if currSum > 9:
                carry = 1
            else:
                carry = 0
            currSum %= 10
            linkSum.val = currSum
            if A is not None or B is not None:
                linkSum.next = ListNode(0)
                linkSum = linkSum.next
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

A = createList([1,1,1,1])
B = createList([9,8,9])
C = createList([1,6,5,8,7,9,7,4,5,2,6,1])
D = createList([384, 183, 463, 31])

s = Solution()
printList(s.addTwoNumbers(A, B))