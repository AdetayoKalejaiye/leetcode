class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        mp = {letter: idx for (idx, letter) in enumerate(letters) }
        output = ''
        for word in words:
            weight = 0
            for letter in word:
                weight += weights[mp[letter]]
            weight %= 26
            output += letters[::-1][weight]
        return output
