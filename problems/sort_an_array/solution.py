class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        ret = []
        while nums:
            ret.append(heappop(nums))
        return ret