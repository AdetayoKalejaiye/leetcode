class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first thought that comes to my head is how I search it naturally, so I look then I check for 101 not there you move to the next 4, 5 is not there, move to 200 if 200 + 1 in...you get it but ti's O(n^2) to make it O(n) I need to make sure that it's the first of the streak

        curr = longest =  0
        check = set(nums)
        n = len(nums)
        #we make nums a set for more efficiency
        for num in check:
            if num -1 not in check: #to confirm that it's the beginning of the streak
                curr = 1
                val = num
                while val + 1 in check:
                    curr += 1
                    val += 1
            longest = max(curr, longest)
        return longest















        #huh get the max()

        # if not nums:
        #     return 0
        # biggest = max(nums)
        # smallest = min(nums) if min(nums) < 0 else 0
        # offset = smallest
        # arr = [0] * (biggest-smallest + 1)
        # n = len(nums)
        # m = biggest -smallest + 1
        # for i in range(n):
        #     arr[nums[i] - offset] += 1

        # longest = 0
        # curr = 0
        # for i in range(m):
        #     if arr[i] != 0:
        #         curr += 1
        #         longest = max(longest, curr)
        #     else:
        #         curr = 0
        # return longest

