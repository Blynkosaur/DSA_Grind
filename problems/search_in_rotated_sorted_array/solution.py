class Solution:
    def binary_search(self, nums, target)->int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        #do two binary searches
        print(nums[0:right], nums[right:])
        first_half = self.binary_search(nums[0:right], target)
        second_half = self.binary_search(nums[right:], target) 
        
        if first_half is not None: return first_half
        elif second_half is not None: return second_half + right
        return -1


        

