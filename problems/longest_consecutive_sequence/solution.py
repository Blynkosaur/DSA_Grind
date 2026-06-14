class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        max_len = 0
        
        for num in hashset:
            if num-1 not in hashset:
                longest = 0
                while (num + longest) in hashset:
                    longest += 1
                    max_len = max(max_len, longest)
        return max_len       

        