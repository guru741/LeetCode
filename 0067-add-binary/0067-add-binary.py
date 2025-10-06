class Solution(object):
    def addBinary(self, a, b):
        a,b = int(a,2),int(b,2)
        c = a + b
        c = format(c,'b')
        return c
        