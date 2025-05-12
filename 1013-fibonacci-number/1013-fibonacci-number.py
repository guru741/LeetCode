class Solution(object):
    def fib(self, n):

        if n == 1:
            return 1
        elif n == 0:
            return 0
        a,b = 1,0
        temp = 0
        for i in range(1,n + 1):
            temp = a + b
            a = b
            b = temp
        return temp

        