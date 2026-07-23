# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findMountainIndex(self, mountain: 'MountainArray')-> int:
        left, right = 0 , mountain.length() - 1
        while left < right:
            mid = left + (right-left)//2
            if mountain.get(mid) < mountain.get(mid+1):
                left = mid + 1
            else:
                right = mid
        return left
            
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findMountainIndex(mountainArr)
        left, right = 0, peak
        #first half ascending
        while left <= right:
            mid = left + (right-left)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left = peak + 1
        right = mountainArr.length()-1
        #second half descending
        while left <= right:
            mid = left + (right-left)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                right = mid - 1
            else:
                left = mid + 1 


        return -1
            
        
        
        