# node of a Singly Linked List
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    # method for setting the data field of the node
    def set_data(self, data):
        self.data = data
    
        