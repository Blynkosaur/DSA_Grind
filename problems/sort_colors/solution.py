class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0)+1
        current = 0 
        print(counter)
        for i in (0,1,2):
            if i not in counter.keys():
                continue
            for j in range(counter[i]):
                nums[current+j] = i
            current += counter[i]
        

                


    
        