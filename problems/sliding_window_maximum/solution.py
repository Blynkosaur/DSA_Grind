class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        ret = []
        for i in range(k):
            if not window:
                window.append((nums[i], i))
                continue
            while window and window[-1][0] < nums[i]:
                window.pop()
            window.append((nums[i],i))
        ret.append(window[0][0])
        start = 1
        for i in range(len(nums)-k):
            new = nums[k+i]
            if window[0][1] < start:
                window.popleft()
            while window and window[-1][0] < new:
                window.pop()
            window.append((new, k+i))
            ret.append(window[0][0])
            start += 1
        return ret



        