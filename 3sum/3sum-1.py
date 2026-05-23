class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #okay, sort nums, l = 0, r = n -1, for i in range(n): then do the search add it to the output set (thereby handling duplicates and tadah?)
        #just keep skipping if the variables are the same
        n = len(nums)
        i = 0
        mid = n //2
        output = []
        nums.sort()
        while i < n:
            #skip targets factored before
            if i > 0 and nums[i] == nums[i-1]: 
                i += 1
                continue
            l = i + 1
            r = n - 1
            target = nums[i]
            while l < r:
                if nums[l] + nums[r] == -target:
                    output.append([nums[l], nums[r], target])
                    #essentially saying if there are duplicates, skip to the last one and then the incrementing code after the while loop essentially makes it go to a new element
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -target:
                    r -= 1
                else:
                    l += 1
                #just to make sure that these lot don't factor in the target as a triplet
                # if l == i:
                #     l += 1
                # if r == i:
                #     r -= 1
            #essentially the same style as the while loop to skip to the last one for l and r
            i += 1

        return output
