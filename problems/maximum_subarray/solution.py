class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        current = 0
        for i in nums:
            if current<0:
                current = 0
            current += i
            if current> global_max:
                global_max = current
        return global_max