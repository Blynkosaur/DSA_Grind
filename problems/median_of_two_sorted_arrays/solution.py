class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1+nums2
        new.sort()
        
        if len(new)%2 ==1:
            return new[int(len(new)/2)]
        else:
            
            return (new[int(len(new)/2)]+new[(int(len(new)/2))-1])/2
                
        
        