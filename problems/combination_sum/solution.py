class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = collections.deque([])
        for i in range(len(candidates)):
            stack.append(([candidates[i]],candidates[i]))
        while stack:
            array = stack.popleft()
            if array[1] == target and sorted(array[0]) not in res:
                res.append(sorted(array[0]))
            elif array[1] < target:
                for el in candidates:
                    temp = array[0].copy()
                    temp.append(el)
                    stack.append((temp,array[1]+el))
            

        return res
                
                