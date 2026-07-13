class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        colLen = len(matrix)
        l, r = 0, rowLen * colLen - 1
        while l <= r:
            mid = (l+r) // 2
            row = mid // rowLen
            col = mid % rowLen
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else: return True
        return False