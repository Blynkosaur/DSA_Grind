class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  
        stack = deque([])
        for i in range(len(nums)):
            stack.append(([nums[i]],i))
        print(stack)
        while stack:
            node = stack.popleft()
            if len(node[0])<= len(nums):
                if sorted(node[0]) not in res:
                    res.append(sorted(node[0]))
                
                start = node[1]+1
                for i in range(start,len(nums)):
                    temp = node[0].copy()
                    temp.append(nums[i])
                    stack.append((temp,i))
        
        return res