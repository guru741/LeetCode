class Solution(object):
    def zeroFilledSubarray(self, nums):
        total,count = 0,0
        for i in nums:
            if i == 0:
                count += 1 
                total += count
            else:
                count = 0
        return total
        