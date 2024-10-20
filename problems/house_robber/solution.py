class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            best = max(dp[i-1],nums[i]+dp[i-2])
            dp.append(best)
        
        return dp[-1]
