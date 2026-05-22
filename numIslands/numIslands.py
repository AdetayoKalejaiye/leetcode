class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #okay...graph, not my strongest spot but can't be that hard....intuitively what I might like to do is add a row of 0 to the beginning and end of the list and add 0 around the ends of each row but that's kind of dumb because of unnecessary overhead, I'll just assume that if the neighbour is None we make it 0

        #make a visited set...you search then every row in the grid for a 1and if (i, j) not in visited, then call your bfs function on it and let's see


        
        visited = set()
        

        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            visited.add((i,j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbours = [
            (i + dr,j + dc) for dr, dc in directions
            if 0 <= i + dr < m and 0 <= j + dc < n
            ]
            for neighbour in neighbours:
                if neighbour not in visited and grid[neighbour[0]][neighbour[1]] == "1":
                    dfs(neighbour[0],neighbour[1])
            
        count = 0
        for i in range(m):
            for j in range(n):
                if not (i, j) in visited and grid[i][j] == "1":
                    print("Hi")
                    count += 1
                    dfs(i, j)
                    
        return count