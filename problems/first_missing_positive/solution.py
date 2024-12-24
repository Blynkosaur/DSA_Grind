class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        heapify(nums)
        while nums:
            num = heappop(nums)
            if num == smallest:
                smallest += 1
        return smallest