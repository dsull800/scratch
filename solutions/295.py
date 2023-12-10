class MedianFinder:

    def __init__(self):
        self.min_heap = [] ## this the where the n // 2 largest elements are stored
        self.max_heap = [] ## this is where the n // 2 smallest elements are stored

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heappush(self.max_heap, -num)

        elif len(self.min_heap) < len(self.max_heap):
            new_num = -heappushpop(self.max_heap, -num)
            heappush(self.min_heap, new_num)
        elif len(self.min_heap) >= len(self.max_heap):
            new_num = heappushpop(self.min_heap, num)
            heappush(self.max_heap, -new_num)



    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()