class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x,y = p
            e_distance = (x**2 + y**2)**0.5
            heapq.heappush(heap, (e_distance * -1, p))
            while len(heap) > k:
                heapq.heappop(heap)
        return [point[1] for point in heap]

        