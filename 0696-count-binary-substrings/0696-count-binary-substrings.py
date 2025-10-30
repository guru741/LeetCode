class Solution(object):
    def countBinarySubstrings(self, s):
        l,count = [],1
        for i in range(len(s) - 1):
            if int(s[i]) == int(s[i + 1]):
                count += 1 
            else:
                l.append(count)
                count = 1
        l.append(count)
        ans = 0
        for i in range(len(l) - 1):
            ans += min(l[i],l[i + 1])
        return ans
        