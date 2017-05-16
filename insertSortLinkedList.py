# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A is None or A.next is None:
            return A
        sorted_list = A
        A = A.next
        sorted_list.next = None
        while A is not None:
            curr = A
            A = A.next
            if curr.val < sorted_list.val:
                # Advance the nodes
                curr.next = sorted_list
                sorted_list = curr
            else:
                search = sorted_list
                while search.next is not None and curr.val > search.next.val:
                    search = search.next
                curr.next = search.next
                search.next = curr
        return sorted_list


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

s = Solution()
printList(s.insertionSortList(A))
printList(s.insertionSortList(B))
printList(s.insertionSortList(C))
