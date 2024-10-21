class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)/2
        for i in range(len(nums)-1,-1,-1):
            newdp = dp.copy()
            for t in newdp:
                if (nums[i]+t) == target:
                    return True
                dp.add(nums[i] +t)
            
        return False