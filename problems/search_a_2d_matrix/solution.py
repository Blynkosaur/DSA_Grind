class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first binary search
        left= 0 
        right = len(matrix)-1
        target_row = []
        while left <= right:
            mid = left + (right-left)//2
            last = matrix[mid][-1]
            first = matrix[mid][0]
            # print(f"mid: {mid}")
            if target >= first and target <= last:
                target_row = matrix[mid]
                break
            elif target > last:
                left = mid + 1
            else:
                right = mid - 1
        # print(f"target_row: {target_row}")
        #second search
        left = 0 
        right = len(target_row) - 1
        while left <= right:
            mid = left + (right - left)//2
            if target_row[mid] == target:
                return True
            elif target_row[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return False


            



        