class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        mod = total%3
        if mod == 0:
            return total
        one = [num for num in nums if num % 3 == 1]
        one.sort()
        two = [num for num in nums if num %3 == 2]
        two.sort()
        if mod == 1:
            if len(one) < 1 and len(two) < 2:
                return 0
            elif len(one) < 1 and len(two) >= 2:
                return total - two[0] - two[1]
            elif len(one) >= 1 and len(two) < 2:
                return total - one[0]
            else:
                return total - one[0] if one[0] < two[0] + two[1] else total -two[0] - two[1]
        elif mod == 2:
            if len(two) < 1 and len(one) < 2:
                return 0
            elif len(two) < 1 and len(one) >= 2:
                return total - one[0] - one[1]
            elif len(two) >= 1 and len(one) < 2:
                return total - two[0]
            else:
                return total - two[0] if two[0] < one[0] + one[1] else total -one[0] - one[1]


        