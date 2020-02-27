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
        # var for current node

        # compare value to root
        # if value == root, return true
        if target == self.value:
            return True
        # if smaller, go left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        # if greater or equal, go right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        # repeat previous two steps until value matches (True)
        # or the next appropriate node == None
        

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

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

        # initialize a stack
        stack = Stack()
        # push root to stack
        stack.push(node)
        # while stack not empty
        while stack.len() > 0:
            # pop top item out of stack into temp
            temp = stack.pop()
            # DO THE THING!!!!!!
            print(temp.value)
            # if temp has right right put into stack
            if temp.right:
                stack.push(temp.right)
            # if temp has left left put into stack
            if temp.left:
                stack.push(temp.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
