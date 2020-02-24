import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        if self.size == 0:
            self.storage.add_to_head(value)
            self.size += 1
        else:
            self.storage.add_to_tail(value)
            self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        elif self.size == 1:
            value = self.storage.head.value
            self.storage.head = None
            self.storage.tail = None
            self.size -= 1
            return value

        else:
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            self.size -= 1
            return value

    def len(self):
        length = 0
        current_node = self.storage.head

        if self.size == 0:
            return 0
            
        else:

            while current_node is not None:
                length += 1
                current_node = current_node.next
            return length
