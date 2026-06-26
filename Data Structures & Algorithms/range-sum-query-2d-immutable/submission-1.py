class NumMatrix:

    #use prefix sum for the O(1) lookup
    #each square has a len(list)^2 sum options
    #the sum will correspond to the va
    def __init__(self, matrix: List[List[int]]):
        matrix = [[0] * (len(matrix[0]) + 1)] + [[0] + row for row in matrix]
        print(matrix)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                matrix[i][j] += matrix[i][j-1] + matrix[i-1][j]-matrix[i-1][j-1]
                self.matrix = matrix
        return None

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #return matrix[row2][col2] - matrix[row1-1][col2]-matrix[row2][col1-1]+matrix[row1-1][col1-1]
        matrix = self.matrix
        return matrix[row2+1][col2+1] - matrix[row1][col2+1]-matrix[row2+1][col1]+matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)