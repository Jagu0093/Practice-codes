def are_adjacent(adj_matrix, node1, node2):
    """
    Function to check if two nodes are adjacent in an undirected graph.
    
    Parameters:
    adj_matrix (list of list): The adjacency matrix of the graph.
    node1 (int): The first node.
    node2 (int): The second node.
    
    Returns:
    bool: True if the nodes are adjacent, False otherwise.
    """
    # Check if the given nodes are within the bounds of the adjacency matrix
    if node1 < 0 or node2 < 0 or node1 >= len(adj_matrix) or node2 >= len(adj_matrix):
        raise ValueError("Node indices are out of bounds of the adjacency matrix.")
    
    # Check if the two nodes are adjacent (i.e., if the value in the matrix is 1)
    return adj_matrix[node1][node2] == 1

# Example usage:
adj_matrix = [
    [1, 1, 0, 0],  # Node 0 is adjacent to Node 1
    [1, 1, 0, 0],  # Node 1 is adjacent to Node 0 and Node 2
    [1, 0, 0, 1],  # Node 2 is adjacent to Node 1 and Node 3
    [0, 0, 1, 1]   # Node 3 is adjacent to Node 2
]

# The 4 nodes to check adjacency between
nodes = [0, 1, 2, 3]
t_count = 0
# Check if any two nodes in the list are adjacent
for i in range(len(nodes)):
    
    for j in range(i + 1, len(nodes)):
       
        node1 = nodes[i]
        node2 = nodes[j]
        result = are_adjacent(adj_matrix, node1, node2)
        if result:
            t_count += 1
        print(f"Nodes {node1} and {node2} are adjacent: {result}")
print(t_count)