
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['M', 'N'],
    'G': ['O', 'P'],
    'H': ['Q', 'R'],
    'I': ['S', 'T'],
    'J': ['U', 'V'],
    'K': ['W', 'X'],
    'L': ['Y', 'Z']
}


visited_nodes = []

def traverseGraph(graph, start_node, visited_nodes : list):
    if start_node not in graph:
        print("This is a dead end")
        return
    visited_nodes.append(start_node)
    print(f'Started at this node: {start_node}.')
    for neighbor in graph[start_node]:
        if neighbor not in visited_nodes:
            print(f'Went to this node: {neighbor}.')
            traverseGraph(graph, neighbor, visited_nodes)
       


traverseGraph(graph,'A', visited_nodes)