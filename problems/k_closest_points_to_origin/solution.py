class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        ret = []
        for i in points:
            toadd = (i[0]**2)+(i[1]**2)
            distances.append((toadd,i))
        heapify(distances)
        for i in range(k):
            distance, point = heappop(distances)
            ret.append(point)
        return ret