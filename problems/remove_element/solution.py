class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)-1
        left = 0
        count = 0
        def move_right():
            nonlocal right, count
            while  right >=0 and nums[right] == val:
                right -= 1
                count += 1
        move_right()
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left] 
                move_right()
            left += 1
                
        
        return len(nums)-count
            
        