class Solution(object):
    def isPowerOfTwo(self, n):
        # if n == 1:
        #     return True
        # if n % 2 != 0 or n <= 0:
        #     return False
        # return self.isPowerOfTwo(n // 2)
        
        return n > 0 and (n & (n - 1)) == 0