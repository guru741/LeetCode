class Solution(object):
    def smallestNumber(self, n):
        return 2 ** n.bit_length() - 1
        