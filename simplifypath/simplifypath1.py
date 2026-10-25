class Solution:
    def simplifyPath(self, path: str) -> str:
        #
        stack = []
        words = path.split("/")
        l = 0
        n = len(words)
        while l < n:
            if words[l] == '':
                l += 1
                continue
            if words[l] == '.':
                l += 1
                continue
            elif words[l] == '..':
                if stack:
                    stack.pop()
                l += 1
                
            else:
                stack.append(words[l])
                l += 1
        output = ''
        if not stack:
            return '/'
        print(stack)
        for word in stack:
            output += f'/{word}'
            

        return output

