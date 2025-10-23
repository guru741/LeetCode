class Solution(object):
    def hasSameDigits(self, s):
        while len(s) > 2:
            ans = ""
            for i in range(len(s) - 1):
                sum_ele = (int(s[i]) + int(s[i + 1])) % 10
                ans += str(sum_ele)
            s = ans
        if s[0] == s[1]:
            return True
        else:
            return False
                
        