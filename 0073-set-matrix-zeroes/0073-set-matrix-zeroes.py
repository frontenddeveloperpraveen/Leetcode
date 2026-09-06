class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        def setRowColZero(mat,row,col):
            for i in range(n):
                if(mat[i][col] != 0):
                    mat[i][col] = -float('inf')
            for i in range(m):
                if(mat[row][i] !=0):
                    mat[row][i] = -float('inf')
        for row in range(n):
            for col in range(m):
                element = matrix[row][col]
                if(element == 0):
                    setRowColZero(matrix,row,col)

        for row in range(n):
            for col in range(m):
                if(matrix[row][col] == -float('inf')):
                    matrix[row][col] = 0
                
        return matrix
        