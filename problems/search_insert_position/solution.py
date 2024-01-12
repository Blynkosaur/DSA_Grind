class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                counter += 1
            
        return counter
    


        