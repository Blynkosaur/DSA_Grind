class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque([])
        length = len(nums)
        res = deque([])
        for el in nums:
            queue.append([el])
        print(queue)
        while queue:
            array = queue.popleft()
            if len(array) == length:
                res.append(array)
            elif len(array) < length:
                for el in nums:
                    temp = array.copy()
                    if el not in temp:
                        temp.append(el)
                        queue.append(temp)
        return res
                    