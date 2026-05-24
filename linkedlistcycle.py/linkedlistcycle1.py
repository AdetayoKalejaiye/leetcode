# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #first thing that comes through my head is have two traversal functions
        #so you define a function that checks if there is a cycle and then in the main function you traverse through the list and call the check function

        #how would the check function work, parameter (node), while the nxt is not equal to none or the node itself, curr =nxt, if nxt is None: return False, if nxt == node: return True

        #there's no breakpoint so that idea was worthless, just put it in a set called visited and see what happens
        if head:
            visited = set()
            curr = head
            while curr.next:
                if curr in visited:
                    return True
                visited.add(curr)
                curr = curr.next
        return False
