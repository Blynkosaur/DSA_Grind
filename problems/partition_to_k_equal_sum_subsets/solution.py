class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # return True
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums)//k
        mask = [False] * len(nums)
        def backtrack(idx, remaining, curr_sum):
            # print(idx, remaining, curr_sum)
            if remaining == 0:
                return True
            if curr_sum == target:
                return backtrack(0, remaining - 1, 0)
            
            for i in range(idx, len(nums)):
                if mask[i] or curr_sum + nums[i] > target:
                    continue
                mask[i] = True
                if backtrack(i + 1, remaining, curr_sum + nums[i]):
                    return True
                mask[i] = False
                if curr_sum == 0:
                    return False
            
            return False
        return backtrack(0, k, 0)
