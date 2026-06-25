class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            running = 0
            for j in range(i, n):
                if nums[j] == target:
                    running += 1
                if running * 2 > (j - i + 1):
                    count += 1
        return count