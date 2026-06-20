class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the middle of the list using the runner technique
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        # 3. Calculate the maximum twin sum
        max_twin = 0
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:
            max_twin = max(max_twin, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_twin
