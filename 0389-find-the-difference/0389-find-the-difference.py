class Solution(object):
    def findTheDifference(self, a,b):
        for c in b:
            if b.count(c) > a.count(c):
                return c        