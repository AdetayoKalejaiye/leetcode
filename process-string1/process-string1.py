class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for lett in s:
            if lett.islower():
                result.append(lett)
            elif lett == '*':
                if result:
                    result.pop()
            elif lett == '#':
                result *= 2
                #this is pythonic but in order languagea I'd use a temp variable then append that list
            elif lett == '%':
                result = result[::-1]
        return ''.join(result)