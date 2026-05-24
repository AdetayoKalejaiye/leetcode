"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#I might be cooked. I might just be cooked.
#Okay, let's take it from the top, traversing ts is easy you could do that in your sleep
#the hard part is I'm not quite sure what they want, to make a clone? What am I? Jesus
#let's just do something that for neighbor in neighbors while processing the dfs (then something happens...wtf happens)
#okay let's just have a variable called nd
#and just say nd = Node(val = node.val, neighbors = dfs(node.neigbors)) and in the dfs what gets returned is Node(val = node.neighbors, neighbors=dfs(node.neihbors))
#obviously needs a visited set and whatever just code, bruv

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # lives outside dfs, shared across all calls

        def dfs(nd):
            if nd in visited:
                return visited[nd]
            
            clone = Node(val=nd.val)  # create node first...
            visited[nd] = clone       # ...register it before recursing (handles cycles) this essentially prevents the issue with your one liner which essentially means that if a neighbor points to the nd, then you'd be cooked since nd doesn't exist yet
            clone.neighbors = [dfs(neighbor) for neighbor in nd.neighbors]
            return clone

        return dfs(node)


                

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         def dfs(nd, visited={}):
#             if visited is None:
#                 visited = {}
            
#             if nd not in visited:
#                 visited[nd] = Node(val=nd.val, neighbors=[dfs(neighbor, visited) for neighbor in nd.neighbors])
            
#             return visited[nd]
#         if node:
            
#             return dfs(node)
#         return None