class Solution(object):
    def reverseWords(self, s):
        s = s.split(' ')
        res = ""
        for i in s:
            k = ''.join(reversed(i))
            res += k + " "
        return res.strip()
        