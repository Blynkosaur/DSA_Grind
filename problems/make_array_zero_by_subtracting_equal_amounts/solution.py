class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while 0 in nums:
            nums.remove(0)
        
        while len(nums)!=0:
            substract = min(nums)
            for i in range(len(nums)):
                nums[i] = nums[i]-substract
            while 0 in nums:
                nums.remove(0)
            operations +=1
            
        return operations
            