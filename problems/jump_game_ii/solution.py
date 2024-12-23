class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(nums[0],0,0)])
        visited= set()
        print(queue)
        while queue:
            layer = queue.popleft()
            print(layer)
            number = layer[0]
            position = layer[1]
            step = layer[2]
            if position == len(nums)-1:
                return step
            for i in range(1,number+1):
                nxt = i + position
                if nxt not in visited and nxt < len(nums):
                    queue.append((nums[position+i],nxt,step +1))
                visited.add(position +i)