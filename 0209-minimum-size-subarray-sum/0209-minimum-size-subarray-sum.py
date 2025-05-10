class Solution(object):
    def minSubArrayLen(self, target, nums):
        i,j,length,sum_ele = 0,0,float('inf'),0
        for j in range(len(nums)):
            sum_ele += nums[j]
            while sum_ele >= target:
                length = min(length,j - i + 1)
                sum_ele -= nums[i]
                i += 1
        return length if length != float('inf') else 0
        