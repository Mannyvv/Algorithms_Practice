
from LinkedList import *

original_linked_list = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
original_linked_list.add_node(node1)
original_linked_list.add_node(node2)
original_linked_list.add_node(node3)

class ReverseLinkedList():
    def __init__(self,):
        self.head = None

    def reverse_linked_list(self,linked_list):
        current_node = linked_list.head
        previous_node = None

