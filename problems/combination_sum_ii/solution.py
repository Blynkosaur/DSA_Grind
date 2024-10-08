class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(array,target,start):
            if target == 0 and sorted(array) not in res:
                res.append(sorted(array))
            else:
                previous = None
                for i in range(start+1,len(candidates)):
                    if candidates[i] != previous and target - candidates[i] >= 0:
                        temp = array.copy()
                        temp.append(candidates[i])
                        helper(temp,target-candidates[i],i)
                        previous = candidates[i]
                        
        helper([],target,-1)
        return res
            