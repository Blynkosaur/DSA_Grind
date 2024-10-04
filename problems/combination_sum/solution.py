class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(array,target):
            copy = array
            if target < 0:
                return 
            elif target == 0 and sorted(array) not in res:
                res.append(sorted(array))
            else:
                for el in candidates:
                    temp = array.copy()
                    temp.append(el)
                    helper(temp,target-el)
                    
        helper([],target)

        return res
                
                