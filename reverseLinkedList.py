## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# step 1: build a linkedlist
# step 2: build a function that reverses the linked list


class Node:
    def __init__(self, val = 0):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        
    def insert(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.end = self.head
        self.end.next = node
        self.end = self.end.next
    
    def get_start(self):
        return self.head.value
    
    def get_end(self):
        return self.end.value
    
    def print_list(self):
        node = self.head
        # print node.value
        while node is not None:
            print node.value,
            node = node.next
    
    
    def reverse_list(self):
        currentNode = self.head
        nextNode = None
        prevNode = None
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        print
        self.head = prevNode
        self.print_list()


linked_list = LinkedList()

for i in range(1, 11):
    linked_list.insert(i)

linked_list.print_list()

linked_list.reverse_list()