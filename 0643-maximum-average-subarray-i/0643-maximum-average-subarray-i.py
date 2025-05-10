class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        sum_ele = sum(nums[:k])
        max_avg = sum_ele / k
        while right < len(nums):
            sum_ele += nums[right] - nums[left]
            max_avg = max(max_avg,sum_ele / k)
            left += 1
            right += 1
        return max_avg