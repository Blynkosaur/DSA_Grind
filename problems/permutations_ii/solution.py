class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        subs = []
        def backtrack(sub ):
            if len(sub) == n:
                subs.append(sub)
                return
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 1
                    backtrack(sub + [c])
                    counter[c] += 1
        backtrack([])
        return subs
                    

        