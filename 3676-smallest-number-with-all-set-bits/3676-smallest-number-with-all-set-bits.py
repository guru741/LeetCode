class Solution(object):
    def smallestNumber(self, n):
        n = bin(n)[2:]
        n = n.replace('0','1')
        return int(n,2)
        