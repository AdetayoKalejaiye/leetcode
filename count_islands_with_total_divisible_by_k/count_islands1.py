class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        #go through everything
        # have a visited set
        # if you land on a non 0 element
        # go for neighbours if it's not out of bounds
        # sum

        visited = set()
        rows = len(grid)
        columns = len(grid[0])
        output = 0
        directions = [(0,1), (-1,0), (1,0), (0,-1)]
        for i in range(rows):
            for j in range(columns):
                if (i, j) not in visited and grid[i][j] != 0:
                    count = 0
                    queue = [(i,j)]
                    while queue:
                        curr = queue.pop()
                        for direction in directions:
                            if 0 <= curr[0] + direction[0] < rows and 0 <= curr[1] + direction[1] < columns and grid[curr[0] + direction[0]][curr[1] + direction[1]] != 0 and (curr[0] + direction[0], curr[1] + direction[1]) not in visited:
                                queue.append((curr[0] + direction[0], curr[1] + direction[1]))
                        count += grid[curr[0]][curr[1]]
                        grid[curr[0]][curr[1]] = 0
                        visited.add((curr[0], curr[1]))
                    if count % k == 0:
                        output += 1
        return output
