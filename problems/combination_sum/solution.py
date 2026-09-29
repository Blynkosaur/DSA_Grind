class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_cand = []
        def backtrack(current_nums, total, last):
            if total > target:
                return
            if total == target:
                all_cand.append(current_nums)
                return
            for c in candidates:
                if c >= last:
                    backtrack(current_nums + [c], total + c, c)
        backtrack([], 0, 0)
        return all_cand
        