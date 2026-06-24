class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_ptr = 0
        curr_counter = 0
        while curr_counter < len(nums):
            nums[unique_ptr] = nums[curr_counter]
            while curr_counter < len(nums) and nums[unique_ptr] == nums[curr_counter]:
                curr_counter += 1
            unique_ptr += 1
        return unique_ptr 

        