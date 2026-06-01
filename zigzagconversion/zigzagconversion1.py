class Solution:
    def convert(self, s: str, numRows: int) -> str:
        container = [[] for _ in range(numRows)]
        down = True
        i = 0
        n = len(s)
        if n == 1:
            return s
        if numRows == 1:
            return s
        while i < n:
            if down:
                for a in range(numRows -1):
                    #don't include bottommost row
                    if i < n:
                        container[a].append(s[i])
                        i += 1
                    else:
                        break
                down = False
            else:
                for b in range(numRows - 1, 0, -1):
                    #include bottommost row
                    if i < n:
                        container[b].append(s[i])
                        i += 1
                    else:
                        break
                down = True
        output = []
        for lst in container:
            output.extend(lst)
        return "".join(output)

        
