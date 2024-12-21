class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums = nums [::-1]
        goal = 0
        for i in range(len(nums)):
            jump = nums[i]
            if i - goal <= jump:
                goal = i
        if goal == len(nums)-1:
            return True
        return False