class Solution(object):
    def transpose(self, mat):
        res = [[0] * len(mat) for _ in range(len(mat[0]))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[j][i] = mat[i][j]
        return res