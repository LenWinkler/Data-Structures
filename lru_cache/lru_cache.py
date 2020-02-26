from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes_in_cache = 0
        self.dll = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check if key in cache
        if key not in self.cache:

            # if not, return None
            return None

        # if it is
        else:
            # create variables
            curr_node = self.dll.head
            value = None

            # search linked list for key:value and move them to front of dll
            while curr_node is not None:
                if curr_node.value == key:
                    self.dll.move_to_front(curr_node)
                    value = self.cache[key]
                    break
                else:
                    curr_node = curr_node.next

            # return value
            return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        print('asdf')
        # create variables
        curr_node = self.dll.head

        # if key already exists in cache, overwrite value with the new value
        if key in self.cache:
            print('before')
            self.cache[key] = value
            print('after', self.cache[key])

            # search for corresponding node and move it to front of dll
            while curr_node is not None:
                if curr_node.value == key:
                    self.dll.move_to_front(curr_node)
                    break
                else:
                    curr_node = curr_node.next
        
        else:
        # if key doesn't exist, check if nodes_in_cache == limit
            if self.nodes_in_cache == self.limit:
                
                # if it is remove lru, add key to head of dll, add key:value to cache
                self.dll.remove_from_tail()
                self.dll.add_to_head(key)
                self.cache[key] = value

        # if it isn't, add key to head of dll and add key:value to cache
            else:
                self.dll.add_to_head(key)
                self.cache[key] = value
                self.nodes_in_cache += 1
                print('add', self.cache)