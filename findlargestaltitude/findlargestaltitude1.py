class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cum = l = 0
        gain.append(0)
        n = len(gain)
        for i in range(n):
            l = gain[i]
            gain[i] = cum
            cum += l
        return max(gain)
            