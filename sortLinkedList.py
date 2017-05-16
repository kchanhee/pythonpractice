# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This is stupid >:(
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        nodes = []
        while A:
            nodes.append(A)
            A = A.next
        nodes.sort(key=lambda x: x.val)
        head = ListNode('dummy')
        result = head

        for node in nodes:
            head.next = node
            head = head.next

        head.next = None
        return result.next

# class Solution:
#     # @param A : head node of linked list
#     # @return the head node in the linked list
#     def sortList(self, A):
#         head = A
#         leftHead = mergeSort(A)
#         return leftHead

# # returns two head nodes of the halves
# def splitListInHalf(A):
#     # We are going to split the nodes in half and apply merge sort.{
#     length = 0 # length of the node so we know when to split
#     head = A
#     while A is not None:
#         length += 1
#         A = A.next
#     A = head
#     if length == 1:
#         return head, None
#     if length == 2:
#         return head, head.next
#     count = 0
#     leftHead = head
#     leftEnd = None # need this to slice the halves        
#     rightHead = None

#     while A is not None:
#         count += 1
#         # Initialize right side
#         if count > length / 2 and rightHead is None:
#             rightHead = A
#             leftEnd.next = None # cut off link
#             break # We found right head. we are done
#         leftEnd = A
#         A = A.next # Advance the list
#     return leftHead, rightHead

# # given left and right head nodes, sort them via merge
# # need to split until they are single nodes
# def mergeSort(head):
#     if head is None or head.next is None:
#         return head
#     leftHead, rightHead = splitListInHalf(head)
#     leftHead = mergeSort(leftHead)
#     rightHead = mergeSort(rightHead)

#     return merge(leftHead, rightHead)


# # merge the sorted lists together
# def merge(left, right):
#     if left is None:
#         return right
#     if right is None:
#         return left

#     # leftHead = left
#     start = temp = ListNode()
#     while left is not None or right is not None:
#         if left.val < right.val:
#             currNode = left
#             left = left.next
#         else:
#             currNode = right
#             right = right.next
#         temp.next = currNode
#     temp.next = right or left
#     return start

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
print "Initial List: "
printList(A)
print "Sorted:" 
printList(s.sortList(A))

print "Initial List:" 
printList(B)
print "Sorted:" 
printList(s.sortList(B))

print "Initial List:"
printList(C)
print "Sorted:"
printList(s.sortList(C))

print "Initial List: %s " % printList(D)
print "Sorted: %s" % printList(s.sortList(D))

