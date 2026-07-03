class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float('inf')
        left = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                smallest = min(smallest, i - left + 1) 
                total -= nums[left]
                left += 1 
        if smallest != float('inf'):
            return smallest 
        return 0
            

        