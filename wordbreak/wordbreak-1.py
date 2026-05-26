class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #I think the break condition should be if it's length is more than the length of s and then append whatever

        result = set()
        n = len(s)
        def backt(current_word, word):
            
            current_word += word

            m = len(current_word)
            
            if m == n:
                result.add(current_word)
                return
            if current_word in result:
                return
            if m > n: #prune
                return
            if current_word != s[0:m]: #prune
                return
            else:
                result.add(current_word)
            
            for word in wordDict: #prune
                backt(current_word, word)

        for wrd in wordDict:
            backt('', wrd)

        if s in result:
            return True
        return False