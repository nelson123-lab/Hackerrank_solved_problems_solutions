class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    # Reverse the linked list
    
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # Function to insert a new node into the begining.
    def push(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node
    
    # Function to print the linked list.


    def printList(self):
        temp = self.head
        l = []
        while(temp):
            l.append(temp.data)
            temp = temp.next
        print(l)
    
    # Function to delete a node from the begining.

# Driver Code
llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

# llist.printList()
llist.reverse()
llist.printList()