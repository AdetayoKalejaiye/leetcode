# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #I say go through it and note the count to the node and then get the dictionary
        #so the index to punish will be max count - n + 1
        #if store[max count - n] store[max count -n].next = store[max count - n + 1].next

        #now the reason for the if is saying that if there is no max count - n we're at head so head so head = head.next
        if not head:
            return 
        
        store = {}

        curr = head
        count = 1
        while curr:
            store[count] = curr
            if curr.next:
                count += 1
            curr = curr.next
            
            
        if count - n in store:
            store[count - n].next = store[count - n + 1].next
        else:
            head = head.next
        
        return head