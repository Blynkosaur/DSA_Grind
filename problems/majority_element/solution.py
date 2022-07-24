class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = int(len(nums)/2)+1
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i] += 1
            if hashmap[i]== majority:
                return i