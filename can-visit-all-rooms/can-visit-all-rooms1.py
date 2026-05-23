class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #okay, since I can do it in any order...the question implies that at least, so what do I do
        #I'd make a function that stores the keys in room[0] in a set keys and then when if room index is not in keys then return False, and then do it and if one of them returns True

        #yh..a visited set is a good idea too, for tracking

        #yh...every was definitely cheating just the first thing that popped in my head
        n = len(rooms)
        every = set(i for i in range(0, n))
        def keysearch(index, keys=None, visited=None):
            if keys is None:
                keys = set()
            if visited is None:
                visited = set()
            visited.add(index)
            for element in rooms[index]:
                keys.add(element)
            
            for key in keys:
                if key not in visited:
                    return keysearch(key, keys, visited)
            if visited == every:
                return True
            return False

        return keysearch(index=0)
            