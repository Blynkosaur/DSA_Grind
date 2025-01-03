class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        amount = int(len(nums)/3)
        hashmap = {}
        ret = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] +=1
        print(hashmap,amount)
        for el in hashmap:
            if hashmap[el] > amount:
                ret.append(el)
        return ret