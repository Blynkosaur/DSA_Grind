class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nextup = 1
        nums = set(nums)
        for n in range(1, max(nums)+1):
            if n in nums:
                nextup += 1
            else:
                return nextup
        return nextup
        