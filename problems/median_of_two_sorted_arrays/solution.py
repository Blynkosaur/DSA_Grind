class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = sorted(nums1 + nums2)
        
        if len(ls)%2 == 1:
            return ls[len(ls)//2]
        else:
            return (ls[len(ls)//2] +ls[(len(ls)//2)-1])/2
        