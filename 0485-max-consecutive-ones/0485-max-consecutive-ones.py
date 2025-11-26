class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count,maxi = 0,0
        for i in nums:
            if i == 1:
                count += 1
                maxi = max(maxi,count)
            else:
                count = 0
        return maxi
        