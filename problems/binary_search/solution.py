class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
        if nums[left] == target:
            return left
        else:
            return -1
        

