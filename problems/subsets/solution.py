class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  
        stack = nums.copy()
        for i in range(len(stack)):
            stack[i] = [stack[i]]
        while stack:
            node = stack.pop(0)
            if len(node)<= len(nums):
                res.append(node)
                start = nums.index(node[-1])+1
                for i in range(start,len(nums)):
                    temp = node.copy()
                    temp.append(nums[i])
                    stack.append(temp)
            
        return res