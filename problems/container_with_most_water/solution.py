class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maximum = (right-left)*min(height[left],height[right])
        while left< right:
            water = (right-left)*min(height[left],height[right])
            maximum = max(water,maximum)
            if height[left] >= height[right]:
               
                right -= 1
            elif height[right] > height[left]:
                
                left += 1
            
                
        return maximum
