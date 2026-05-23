class Solution:
    def dfs(self, rooms, i, closed):
        if not closed[i]:
            return 

        closed[i]  = False

        for val in rooms[i]:
            self.dfs(rooms, val, closed)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        closed = [True] * n
        
        self.dfs(rooms, 0, closed)
        
        return not any(closed)
        
        