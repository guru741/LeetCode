class Solution(object):
    def setZeroes(self, matrix):
        rows,cols = len(matrix),len(matrix[0])
        ans = [row[:] for row in matrix]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for row in range(rows):
                        ans[row][j] = 0
                    for col in range(cols):
                        ans[i][col] = 0
                    
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = ans[i][j]

        