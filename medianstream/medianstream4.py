class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush_max(self.maxHeap, heappushpop(self.minHeap, num))
        else:
            heapq.heappush(self.minHeap, heappushpop_max(self.maxHeap, num))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0])/2
        else:
            return self.maxHeap[0]