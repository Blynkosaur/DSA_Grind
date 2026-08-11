class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        total = []
        def backtrack(sub, previous):
            if len(sub) == k:
                total.append(sub)
                return
            for i in range(previous + 1, n + 1):
                backtrack(sub + [i], i)
        backtrack([], 0)
        return total
            


        