class Solution:
    def maxArea(self, height: List[int]) -> int:
        #immediately, my idea is area is essentialyl just (l -r) * min(height[l], height[r]) so I want to maximize l-r and minimize the diff between height[l] and height[r]...not sure how to do it but that's the gist of things
        
        #now a brute force isn't possible because of the 10^5
        #what if we do like idk...not binary search but the style essentially making those two pointers meet and cross in the middle and the loop then ends
        l = 0
        n = len(height)
        r = n - 1
        max_area = float('-inf')
        while l < r:
            area = (r - l) * min(height[l], height[r]) 
            max_area = max(area, max_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
