class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums)-k+1):
            num = heappop(nums)
        return num