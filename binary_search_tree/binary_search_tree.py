import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # var for current node
        current_node = self
        
        # Compare value to root
        # If value is smaller:
        if value < current_node.value:

            # look left, if node:
            if self.left is not None:
                # move there and repeat steps
                current_node = self.left
                current_node.insert(value)
            # if no node:
            else:
                # make new one with this value
                self.left = BinarySearchTree(value)
        # if value is greater or equal:
        elif value >= current_node.value:
            # look right, if node:
            if self.right is not None:
                # move there and repeat steps
                current_node = self.right
                current_node.insert(value)
            # if no node:
            else:
                # make new node with this value
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass
        # if no root:
            # return False
        # else compare value to root
        # if smaller, go left
        # if greater or equal, go right


    # Return the maximum value found in the tree
    def get_max(self):
        pass
        # while you can go right, go right
        # if no right child, return this value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
