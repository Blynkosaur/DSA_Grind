class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #range : min(piles), max(piles)
        piles.sort()
        left = 1
        right = max(piles)

        def hourCount(piles, k):
            hourCounter = 0
            for e in piles:
                hourCounter += ceil(e / k)
            return hourCounter

        while left <= right:
            middle = (left + right)//2
            tempHour = hourCount(piles, middle)
            if (tempHour) <= h:
                # if tempHour == h and hourCount(piles, middle - 1) > tempHour:
                #     return middle
                right = middle - 1
            else:
                left = middle + 1
                print(left,right)
        return left

        