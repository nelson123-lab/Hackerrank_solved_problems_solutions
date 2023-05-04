class Node:             #represents an element in the linkedlist
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next # pointer to next element.

class LinkedList:
    def __init__(self):
        self.head = None # points to head of the linkedlist

    #Insert at begining
    def insert_beging(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist  += str(itr.data) + "-->"
            itr = itr.next
        print(llist)

    def insert_at_end(self, data):      #To insert element at the end.
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):     # TO insert list of element at a time.
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):           #To find the length of linkedlist
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):     #TO remove a value a specific index
        if index <0 or index >=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_Index_data(self, index, data):           #To insert an elment at a specific index
        if index<0 or index >= self.get_length():
            raise Exception("invalid index")

        if index ==0:
            self.insert_beging(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['Age','Colour','Skin'])
    ll.insert_at_end(3)
    ll.insert_beging(5)
    ll.remove_at(2)
    ll.insert_Index_data(2,"Hello")
    ll.insert_Index_data(3,"Hello")
    ll.print()
    print("length",ll.get_length())
