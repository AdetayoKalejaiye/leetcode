class MedianFinder:

    def __init__(self):
        self.stream = []
        

    def addNum(self, num: int) -> None:
        low = 0
        high = len(self.stream) - 1  
        
        while low <= high:
            mid = (low + high) // 2
            if self.stream[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        self.stream.insert(low, num)
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