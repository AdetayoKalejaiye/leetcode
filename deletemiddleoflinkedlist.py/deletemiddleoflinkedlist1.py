# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = -1 #to make this zero indexed
        node = head
        while node:
            count += 1
            node = node.next
        if count % 2 == 1:
            mid = count/2
            mid += 0.5
        else:
            mid = count/2
        if count == 0:
            return head.next
        count = -1
        node = head
        #reset everything
        
        while node:
            count += 1
            if count == mid -1:
                node.next = node.next.next
                break
            node = node.next
        return head