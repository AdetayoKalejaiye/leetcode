class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        n = len(binary)
        if n != 32:
            zeroes = '0' * (32-n)
            binary = zeroes + binary
        return int(binary[::-1], 2)
