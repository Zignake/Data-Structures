class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node

    def insert_at(self, data, index):
        if index > self.length() or index < 0:
            raise Exception('Invalid Index')
            
        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.length():
            self.insert_at_end(data)
            return

        itr = self.head
        counter = 0
        while counter < index-1:
            itr = itr.next
            counter += 1
        node = Node(data, itr.next)
        itr.next = node

    def remove_at(self, index):
        if index >= self.length() or index < 0:
            raise Exception('Invalid Index')
    
        if index == 0:
            itr = self.head
            self.head = itr.next
            return
        
        itr = self.head
        counter = 0
        while counter < index-1:
            itr = itr.next
            counter += 1
        itr.next = itr.next.next

    def insert_values(self, data_list):
        if type(data_list) is not list:
            raise Exception("Entered data is not of type 'list'")

        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, prev, data):
        itr = self.head
        while itr:
            if itr.data == prev:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next
        raise Exception('Given value not in Linked List')

    def remove_by_value(self, value):
        itr = self.head
        if self.head is not None:
            if itr.data == value:
                self.head = itr.next
                return

        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise Exception('Given value not in Linked List')

    def length(self):
        itr = self.head
        counter = 0
        while itr:
            itr = itr.next
            counter += 1
        return counter

    def print(self):
        if self.head is None:
            print('Empty List')
            return 
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' - '
            itr = itr.next
        print(llstr)


# class DNode:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev

# class DoublyLinkedList():
#     def __init__(self,  )


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning('hell')
    # ll.insert_at_beginning('worl')
    # ll.insert_at_end('endddd')
    # ll.print()
    # ll.insert_at('bichme', 0)
    # print(ll.length())
    # ll.print()
    # ll.remove_at(0)
    # ll.print()
    # ll.insert_values(['a', 'b', 'd'])
    # ll.print()
    # ll.insert_after_value('a', 'c')
    # ll.print()
    ll.remove_by_value('a')
    ll.print()