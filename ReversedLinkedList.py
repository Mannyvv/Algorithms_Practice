
from LinkedList import *

original_linked_list = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
original_linked_list.add_node(node1)
original_linked_list.add_node(node2)
original_linked_list.add_node(node3)

def reverse_linked_list(linked_list):
    current_node = linked_list.head
    previous_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    head = previous_node
    return head
    
reverse_head = reverse_linked_list(original_linked_list)
print(reverse_head.next_node.next_node.data)




