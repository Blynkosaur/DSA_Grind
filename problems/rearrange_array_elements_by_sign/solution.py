class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for i in nums:
            if i> 0:
                pos.append(i)
            elif i<0:
                neg.append(i)
        for i in range(len(neg)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans