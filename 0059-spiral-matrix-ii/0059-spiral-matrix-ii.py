class Solution(object):
    def generateMatrix(self, n):
        mat = [[0] * n for _ in range(n)]
        left,right,top,bottom = 0,n - 1,0,n - 1
        num = 1

        while top <= bottom  and left <= right:
            # left to right
            for i in range(left,right + 1):
                mat[top][i] = num
                num += 1
            top += 1

            # top to bottom 
            for i in range(top,bottom + 1):
                mat[i][right] = num
                num += 1
            right -= 1

            # right to left
            if top <= bottom:
                for i in range(right,left - 1,-1):
                    mat[bottom][i] = num
                    num += 1
                bottom -= 1
            
            # bottom to top
            if left <= right:
                for i in range(bottom,top - 1,-1):
                    mat[i][left] = num
                    num += 1
                left += 1
        return mat
        