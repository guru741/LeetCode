class Solution(object):
    def isToeplitzMatrix(self,mat):
        row,col = len(mat),len(mat[0])
        
        for i in range(row - 1):
            for j in range(col - 1):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False
        
        return True