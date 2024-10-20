class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
       
        dp1 = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)-1):
            best = max(nums[i]+dp1[i-2],dp1[i-1])
            dp1.append(best)
        dp2 = [nums[-1],max(nums[-1],nums[-2])]
        for i in range(3,len(nums)):
            best = max(dp2[i-2],nums[-i]+dp2[i-3])
            dp2.append(best)
        return max(dp1[-1],dp2[-1])