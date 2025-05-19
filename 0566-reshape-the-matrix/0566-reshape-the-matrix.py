class Solution(object):
    def matrixReshape(self, mat, r, c):
        res = [[0] * c for _ in range(r)]
        row,col = len(mat),len(mat[0])
        x,y = 0,0
        if (row * col != r * c):
            return mat
            
        for i in range(row):
            for j in range(col):
                res[x][y] = mat[i][j]
                y += 1

                if y == c:
                    y = 0
                    x += 1
        return res