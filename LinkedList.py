class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None



class LinkedList():
    def __init__(self):
        self.head = None
        
    

    def add_node(self,new_node):
        
        #If head is absent, new node becomes head
        if self.head is None:
            self.head = new_node
            self.list_data()
            return

        #if head is present, add node to the latest node
        current_node = self.head

        while current_node.next_node:
            current_node = current_node.next_node
          
        current_node.next_node = new_node

        self.list_data()

    def list_data(self):
        
        current_node = self.head
        list_of_data = []
        while current_node:
            list_of_data.append(current_node.data)
            current_node = current_node.next_node
        print("Data in each node: " , list_of_data)

# offical_linked_list = LinkedList()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# offical_linked_list.add_node(node1)
# offical_linked_list.add_node(node2)
# offical_linked_list.add_node(node3)

