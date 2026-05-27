class Solution:
    def getSum(self, a: int, b: int) -> int:
        from math import log2
            
        # just trying to turn log e^a  into aloge e and remember logarithm rules
     
      
        return int(round(log2(2**a * 2**b)))