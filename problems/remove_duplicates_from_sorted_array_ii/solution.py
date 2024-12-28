class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        print(hashmap)
        for num in hashmap:
            for i in range(hashmap[num]-2):
                nums.remove(num)
        