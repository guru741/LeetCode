class Solution(object):
    def diagonalSum(self, mat):
        sum_ele = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or (i + j) == len(mat) - 1:
                    sum_ele += mat[i][j]
        return sum_ele