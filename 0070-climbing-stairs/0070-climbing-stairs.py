class Solution(object):
    def climbStairs(self, n):
        a,b,c = 1,0,0
        for i in range(n):
            c = a + b
            b = a
            a = c
        return c
        