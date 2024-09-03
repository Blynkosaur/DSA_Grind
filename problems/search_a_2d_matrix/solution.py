class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for el in matrix:
            if target in el:
                return True
        return False