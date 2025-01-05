def are_adjacent(adj_matrix, node1, node2):
    # Check if the matrix is a valid 2D list and node indices are within bounds
    if not all(isinstance(row, list) for row in adj_matrix):
        raise ValueError("Adjacency matrix should be a 2D list.")
    if not (0 <= node1 < len(adj_matrix) and 0 <= node2 < len(adj_matrix)):
        raise ValueError(f"Node indices should be between 0 and {len(adj_matrix) - 1}.")
    
    # Check if there is an edge from node1 to node2
    return adj_matrix[node1][node2] == 1

# Example usage:
adj_matrix = [
    [1, 1, 0, 0],  # Node 0 is adjacent to Node 1
    [1, 1, 0, 0],  # Node 1 is adjacent to Node 0 and Node 2
    [1, 0, 0, 1],  # Node 2 is adjacent to Node 1 and Node 3
    [0, 0, 1, 1]   # Node 3 is adjacent to Node 2
]

node1 = 0
node2 = 1
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        print(i,j)
        if adj_matrix[i][j] == 1:
            print(i,j,"are adjacent",adj_matrix[i][j] == 1)
        #print(i,j,"are adjacent",adj_matrix[i][j] == 1)
