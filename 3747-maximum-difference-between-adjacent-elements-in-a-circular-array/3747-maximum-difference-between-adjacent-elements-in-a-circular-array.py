class Solution(object):
    def maxAdjacentDistance(self, nums):
        maxi = 0
        for i in range(1,len(nums)):
            maxi = max(abs(nums[i] - nums[i - 1]),maxi)
        maxi = max(abs(nums[len(nums) - 1] - nums[0]),maxi)

        return maxi
        