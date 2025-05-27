class Solution(object):
    def differenceOfSums(self, n, m):
        withsum,withoutsum = 0,0
        for i in range(1,n + 1):
            if i % m == 0:
                withsum += i
            else:
                withoutsum += i
        ans = withoutsum - withsum
        return ans
        
        