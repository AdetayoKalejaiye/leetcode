# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #I could just find the middle of the linked list make everything before that double linked by assigning it as previous and then here we go

        count = 1
        node = head
        while node.next:
            count += 1
            node.next.prev = node
            node = node.next
        mid = count / 2
        node = head 
        head.prev = None
        max_twin = float('-inf')
        while node.next:
            count -= 1
            if count == mid:
                new = node.next
                break
            node = node.next
        while new and node:
            max_twin = max(max_twin, new.val + node.val)    
            new = new.next
            node = node.prev
        return max_twin
