def get_region_sizes(matrix):
    if not matrix or not matrix[0]:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = set()
    output = []
    
    # Outer double for-loop to scan the image row by row, column by column
    for i in range(rows):
        for j in range(cols):
            # Check if candidate is a foreground pixel and hasn't been visited yet
            if matrix[i][j] == 1 and (i, j) not in visited:
                
                # Start of your BFS logic
                region_size = 0
                queue = [(i, j)]
                visited.add((i, j))  # Mark visited immediately when queued
                
                while queue:
                    # Pop the first element (FIFO)
                    curr_i, curr_j = queue.pop(0)
                    region_size += 1  # Increment the region counter
                    
                    # Check all 4 directions (Up, Down, Left, Right)
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    
                    for di, dj in directions:
                        next_i, next_j = curr_i + di, curr_j + dj
                        
                        # Safety checks to prevent indexing past assigned grid boundaries
                        if 0 <= next_i < rows and 0 <= next_j < cols:
                            # Evaluate if neighbor is 1 and not already visited
                            if matrix[next_i][next_j] == 1 and (next_i, next_j) not in visited:
                                visited.add((next_i, next_j)) # Prevent duplicates
                                queue.append((next_i, next_j))
                
                # Once the queue is empty, append the region's total size to output
                output.append(region_size)
                
    return output

# --- Example Usage ---
example_matrix = [,
 ,
 ,
 ,
    [1, 1, 0, 0, 0]
]

print(get_region_sizes(example_matrix))
# Output: [3, 5, 4]
