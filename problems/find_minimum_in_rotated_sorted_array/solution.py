class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[left-1]:
                left = mid +1
            elif nums[mid] < nums[right]:
                right = mid
            print(mid,left,right)
        return nums[left]