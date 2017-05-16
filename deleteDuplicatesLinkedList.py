# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        # List is sorted so all that's necessary is to set next pointer to the
        # first pointer that's different and reset the head.
        
        if A is None or A.next is None:
            return A


        curr = A
        head = curr
        seen_vals = {head.val : 1}
        A = A.next
        while A is not None:
            if A.val not in seen_vals:
                seen_vals[A.val] = 1
            else:
                seen_vals[A.val] += 1
            if curr.val != A.val: # not duplicate
                curr.next = A
                curr = curr.next
            else:
                curr.next = None
            A = A.next

        curr = head

        print seen_vals

        # printList(head)
        distinct = None
        distinct_head = distinct
        while curr is not None:
            
            if seen_vals[curr.val] == 1:
                # print "%d is a distinct value." % curr.val
                if distinct is None:
                    distinct = ListNode(curr.val)
                    distinct_head = distinct
                else:
                    distinct.next = ListNode(curr.val)
                    distinct = distinct.next
            curr = curr.next
        return distinct_head

        


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
A = createList([1,1,1,2,2,3,3,4,4,5])
B = createList([1,1,2,3,4,4,4,4,4,4])
C = createList([1,2,3])
s = Solution()
# printList(s.deleteDuplicates(A))
printList(s.deleteDuplicates(B))
# printList(s.deleteDuplicates(C))
