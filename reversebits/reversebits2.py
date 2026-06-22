class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        n = len(binary)
        if n != 32:
            zeroes = '0' * (32-n)
            binary = zeroes + binary
        decimal = binary[::-1]
        n = len(decimal)
        return sum([2**(n - i -1) for i in range(len(decimal)) if decimal[i] == '1'])