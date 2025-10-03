class Solution(object):
    def lengthOfLastWord(self, s):
        ans = s.strip().split()
        if ans:
            return len(ans[-1])
        else:
            return 0
        