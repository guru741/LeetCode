class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        sum_ele = 0
        for i in range(n):
            sum_ele += mat[i][i]
            sum_ele += mat[i][n - 1 - i]
        
        if n % 2 == 1:
            sum_ele -= mat[n / 2][n / 2]

        return sum_ele 


        # sum_ele = 0
        # for i in range(len(mat)):
        #     for j in range(len(mat)):
        #         if i == j or (i + j) == len(mat) - 1:
        #             sum_ele += mat[i][j]
        # return sum_ele