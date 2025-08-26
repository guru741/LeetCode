class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        maxi,ans = 0,0
        for i,j in dimensions:
            square = i * i + j * j
            if square > maxi or square == maxi and i * j > ans:
                maxi = square
                ans = i * j
        return ans