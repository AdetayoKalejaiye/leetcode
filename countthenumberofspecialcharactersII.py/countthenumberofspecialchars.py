import string
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        check = set()
        #hmm reverse the string, and then check for letter in word if not lower contineu
        revword = word[::-1]
        output = 0
        n = len(word)
        for letter in word:
            if letter in check:
                continue
            if letter.isupper():
                if word.find(letter) > n - revword.find(letter.lower()) -1 :
                    output += 1
                    check.add(letter)
                    check.add(letter.lower())
            else:
                continue
        return output