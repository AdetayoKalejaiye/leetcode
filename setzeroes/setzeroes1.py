class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #traverse matrix, if it's 0 make everyr row and column zero, but for efficiency if not str(index) + c in cache do columns add 1if not str(ind)

        cache = set()
        transformed = set()
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m:
            for j in range(n):
                if matrix[i][j] == 0 and not (i, j) in transformed:
                    if f'{j}c'in cache and f'{i}r' in cache:
                        continue
                    if  f'{i}r' not in cache:
                        for a in range(n):
                            if matrix[i][a] != 0:
                                matrix[i][a] = 0
                                transformed.add((i, a))
                        cache.add(f'{i}r')
                    if f'{j}c' not in cache:
                        for row in range(m):
                            if matrix[row][j] != 0:
                                matrix[row][j] = 0
                                transformed.add((row, j))
                        cache.add(f'{j}c')
            i += 1
        