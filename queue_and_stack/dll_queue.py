import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if self.size == 0:
            self.storage.add_to_head(value)
            self.size += 1
        else:
            self.storage.add_to_tail(value)
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        elif self.size == 1:
            value = self.storage.head.value
            self.storage.head = None
            self.storage.tail = None
            self.size -= 1
            return value
            
        else:
            value = self.storage.head.value
            self.storage.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size
