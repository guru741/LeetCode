class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n % 3 != 0 or n <= 0:
            return False
        return self.isPowerOfThree(n // 3)
        