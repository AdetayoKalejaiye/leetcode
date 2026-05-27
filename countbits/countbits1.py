class Solution:
    def countBits(self, n: int) -> List[int]:
        #bin outputs a string with 0x<random whatever

        return [bin(i).count('1') for i in range(n+1)]