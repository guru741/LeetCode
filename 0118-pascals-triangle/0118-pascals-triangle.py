class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            ans = [1] * (i + 1)
            for j in range(1,i):
                ans[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(ans)
        return res
        