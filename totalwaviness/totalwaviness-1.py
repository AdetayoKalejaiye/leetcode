class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        output = 0
        for num in range(num1, num2 + 1):
            nm = str(num)
            l, m, r = 0, 1, 2
            n = len(str(num))
            if n < 3:
                continue
            while r < n:

                if nm[l] < nm[m] > nm[r] or nm[l] > nm[m] < nm[r]:
                    output += 1
                l += 1
                m += 1
                r += 1
                
        return output