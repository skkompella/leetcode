class MedianFinder:

    def __init__(self):
        self.lo_heap = []
        self.hi_heap = []

    def addNum(self, num: int) -> None:
        lo_max=float('inf')
        if self.lo_heap:
            lo_max = -self.lo_heap[0]
        if num < lo_max:
            heapq.heappush(self.lo_heap, -num)
            if len(self.lo_heap)>len(self.hi_heap)+1:
                heapq.heappush(self.hi_heap, -heapq.heappop(self.lo_heap))
                self.flag = 0
        else:
            heapq.heappush(self.hi_heap, num)
            if len(self.hi_heap)>len(self.lo_heap):
                heapq.heappush(self.lo_heap, -heapq.heappop(self.hi_heap))
                self.flag = 1
        
    

    def findMedian(self) -> float:
        if len(self.lo_heap)>len(self.hi_heap):
            return -self.lo_heap[0]
        else:
            if not self.lo_heap:
                return self.hi_heap[0]
            elif not self.hi_heap:
                return -self.lo_heap[0]
            return (-self.lo_heap[0] + self.hi_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
