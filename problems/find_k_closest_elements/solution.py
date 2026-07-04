class Solution:
       def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x)  # first index with arr[i] >= x
        left = right - 1                     # window is arr[left+1 : right], empty
        
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(x - arr[left]) <= abs(x - arr[right]):
                left -= 1   # ties go left (smaller element)
            else:
                right += 1
        
        return arr[left+1:right] 