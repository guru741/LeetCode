class Solution(object):
    def findMaxAverage(self, nums, k):
        left,right,max_avg,sum_ele = 0,0,float('-inf'),0
        while right < len(nums):
            sum_ele += nums[right]
            if (right - left + 1) < k:
                right += 1
            elif (right - left + 1) == k:
                max_avg = max(max_avg,sum_ele)
                sum_ele -= nums[left]
                left += 1
                right += 1
        return float(max_avg) / float(k)

        