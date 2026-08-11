class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        def backtrack(i, subset):
            if i == n:
                subsets.append(subset)
                return
            added = subset + [nums[i]]
            backtrack(i + 1, subset)
            backtrack(i + 1, added)
        backtrack(0, [])
        return subsets
            
