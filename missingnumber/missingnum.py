class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        diff = set(i for i in range(n + 1)).difference(set(nums))
        for element in diff:
            return element