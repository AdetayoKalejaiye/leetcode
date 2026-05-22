from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = sorted(Counter(nums).items(), key = lambda x: -x[1])
        output = []
        for i in range(k):
            output.append(cntr[i][0])
        return output

