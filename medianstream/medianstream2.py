class MedianFinder:

    def __init__(self):
        self.stream = []
        

    def addNum(self, num: int) -> None:
        lo, hi = 0, len(self.stream)

        while lo < hi:
            mid = (lo + hi) // 2

            if num < self.stream[mid]:
                hi = mid
            else:
                lo = mid + 1
        
        self.stream.insert(lo, num)

    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2] + self.stream[n//2 - 1])/2
        else:
            return self.stream[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()