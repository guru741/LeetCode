class Solution(object):
    def plusOne(self, digits):
        temp = int(''.join(map(str,digits)))
        temp = temp + 1
        res = [int(i) for i in str(temp)]
        return res