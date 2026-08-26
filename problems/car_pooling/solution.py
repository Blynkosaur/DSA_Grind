class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for t in trips:
            count, start, end = t
            heapq.heappush(heap, (start, count))
            heapq.heappush(heap, (end, -1 * count))
        head_count = 0
        while heap:
            place, count = heapq.heappop(heap)
            head_count += count
            if head_count > capacity:
                return False
        return True
        

        