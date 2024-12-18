class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones)>1:
            one = heappop(stones)
            two = heappop(stones)
            print(one,two)
            if one != two:
                heappush(stones,-1*abs(two-one))
        if not stones:
            return 0
        return -stones[0]