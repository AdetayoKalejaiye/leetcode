class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Phase 1: track lengths
        lengths = [0]
        for c in s:
            l = lengths[-1]
            if c == '*':   lengths.append(max(0, l-1))
            elif c == '#': lengths.append(l * 2)
            elif c == '%': lengths.append(l)
            else:          lengths.append(l + 1)
        
        if k >= lengths[-1]:
            return '.'
        
        # Phase 2: walk back
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            prev_len = lengths[i]
            cur_len  = lengths[i+1]
            
            if c == '#':
                k = k % prev_len
            elif c == '%':
                k = (cur_len - 1) - k
            elif c == '*':
                pass  # k unchanged
            else:  # letter
                if k == cur_len - 1:
                    return c
                # else k unchanged
        
        return '.'  # shouldn't reach