# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #okay, first thought that comes to my head is have a pointer at the start and have a pointer at the end
        #a list to keep them and then you intialize start and curr

        

        stack = deque()
        node = head
        while node:
            stack.append(node)
            node = node.next
        start = curr = ListNode()
        while stack:
            curr.next = stack.popleft()
            curr = curr.next
            if not stack:
                break
            curr.next = stack.pop()
            curr = curr.next

        #to ensure there's no cycle always make curr.next = None for the last node
        curr.next = None
            
        return start.next