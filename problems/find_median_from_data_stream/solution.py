class MedianFinder:

    def __init__(self):
        self.count = 0
        self.min_half = [] 
        self.max_half = []
        heapify(self.min_half)
        heapify(self.max_half)
        

    def addNum(self, num: int) -> None:
        if not self.count:
            self.count += 1
            heapq.heappush(self.max_half, num)
            return
        self.count += 1
        if num > self.max_half[0]:
            heapq.heappush(self.max_half, num)
        else:
            heapq.heappush(self.min_half, num * -1)
        if self.count % 2:
            while len(self.max_half) > self.count//2 + 1:
                val = heapq.heappop(self.max_half)
                heapq.heappush(self.min_half, val * -1)
            while len(self.min_half) > self.count//2:
                val = heapq.heappop(self.min_half)
                heapq.heappush(self.max_half, val * -1)
        else:
            while len(self.max_half) > self.count / 2:
                val = heapq.heappop(self.max_half)
                heapq.heappush(self.min_half, val * -1)
            while len(self.min_half) < self.count/2:
                val = heapq.heappop(self.min_half)
                heapq.heappush(self.max_half, val * -1)
        

    def findMedian(self) -> float:
        if self.count%2:
            return self.max_half[0]
        return (self.max_half[0] + (self.min_half[0] * -1))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()