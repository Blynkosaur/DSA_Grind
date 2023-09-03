class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #new = []
        # previous = None
        # for num in nums:
        #     if num != previous:
        #         new.append(num)
        #     previous = num
        previous = None
        current= 0
        unique =0 
        for num in nums:
            if num != previous:
                nums[current]= num
                current += 1
                previous = num
                unique += 1
        return unique
        




    