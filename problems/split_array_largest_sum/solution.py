class Solution:
    def possible(self, nums:[List[int]], target_sum: int) -> int:
        k = 0
        curr_sum = 0 
        for num in nums:
            if curr_sum + num <= target_sum:
                curr_sum += num
            else:
                k += 1
                curr_sum = num
        return k + 1
                
    def splitArray(self, nums: List[int], k: int) -> int:
        max_sum = sum(nums)
        min_sum = max(nums)
        glob = max_sum
        while min_sum <= max_sum:
            mid = min_sum + (max_sum - min_sum)//2
            possible = self.possible(nums,mid)
            # print(f"min{min_sum}, max{max_sum}, mid{mid}, possible{possible}")
            if possible <= k:
                glob = min(glob,mid)
                max_sum = mid - 1
            else:
                min_sum = mid + 1
        return glob