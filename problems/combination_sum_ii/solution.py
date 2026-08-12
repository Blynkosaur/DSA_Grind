class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subs = []
        counter = defaultdict(int) 
        for c in candidates:
            counter[c] += 1 
        def backtrack(total, sub, previous):
            if total > target:
                return
            if total == target:
                subs.append(sub)
                return
            for c in counter:
                if counter[c] > 0 and c >= previous:
                    counter[c] -= 1
                    backtrack(total + c, sub + [c], c)
                    counter[c] += 1
        backtrack(0, [], 0)
        return subs 

            
        