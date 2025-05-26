class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if x == 1:
            return 1.0
        if x == -1 and n % 2 == 0:
            return 1.0
        if x == -1 and n % 2 != 0:
            return -1.0
        
        binary = n
        if n < 0:
            x = 1 / x
            binary = -binary
        
        ans = 1
        while binary > 0:
            if binary % 2 == 1:
                ans *= x
            x *= x
            binary //= 2
        return ans
        
       
        
