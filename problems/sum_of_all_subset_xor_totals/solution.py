class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        xor_total = 0
        def backtrack(i, total):
            nonlocal xor_total
            if i == n:
                xor_total += total
                return
            backtrack(i + 1, total ^ nums[i])
            backtrack(i + 1, total)
        backtrack(0, 0)
        return xor_total

            


                