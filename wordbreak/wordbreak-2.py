class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #I think the break condition should be if it's length is more than the length of s and then append whatever

        cache = {}
        def dp(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]  # ✅
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dp(i + len(word)):
                        cache[i] = True  # ✅
                        return True
            
            cache[i] = False  # ✅
            return False
        
        return dp(0)