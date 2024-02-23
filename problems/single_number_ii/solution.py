class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        hash = {}
        for el in nums:
            if el not in hash:
                hash[el] = 1
            else:
                hash[el]+=1
        for h in hash:
            if hash[h] ==1:
                return h
            


                