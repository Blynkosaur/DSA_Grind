class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #check for overlap
        A, B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A
        total_len = len(A) + len(B)
        half = total_len//2
        left = 0
        right = len(A) -1 
        while True:
            mid1 = (left+right)//2
            mid2 = half - mid1 - 2
            A_left = float('-inf') if mid1 < 0 else A[mid1]
            A_right = float('inf') if mid1 + 1 >= len(A) else A[mid1 + 1]
            B_left = float('-inf') if mid2 < 0 else B[mid2] 
            B_right = float('inf') if mid2 + 1 >= len(B) else B[mid2 + 1]

            #correct partition 
            if A_left <= B_right and B_left <= A_right:
                if total_len % 2: 
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right))/2

            elif A_left > B_right:
                right = mid1 -1 
            else:
                left = mid1 + 1

        
            
            
        
        


            




        
        
        
