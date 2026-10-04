class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(p)
        sorted_word = sorted(p)
        length = len(s)
        output = []
        for i in range(0, length - n + 1):
            if sorted(s[i:i+n]) == sorted_word:
                output.append(i)
        return output