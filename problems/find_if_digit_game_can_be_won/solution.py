class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for num in nums:
            if num >= 10:
                double += num
            else:
                single += num
        return not single == double