class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #stack, go through it if it's opening add the closening to the stack and if it matches pop() else return False

        #let's think through it, 


        for char in s:
            if char == '[':
                stack.append(']')
            elif char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            else:
                if stack:
                    if char != stack.pop():
                        return False
                else:
                    return False
        if stack:
            return False
        return True
