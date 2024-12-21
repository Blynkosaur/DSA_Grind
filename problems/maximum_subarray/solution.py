class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        current = 0
        for i in nums:
            if current <0:
                current = 0
                current += i
            else:
                current += i
            maximum = max(maximum,current)
        return maximum