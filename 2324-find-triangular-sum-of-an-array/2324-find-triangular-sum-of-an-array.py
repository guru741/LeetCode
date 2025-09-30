class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        if n == 1:
            return int(''.join(map(str,nums)))
        while n > 1:
            newArray = []
            for i in range(n - 1):
                sum_ele = (nums[i] + nums[i + 1]) % 10
                newArray.append(sum_ele)
            n = len(newArray)
            nums = newArray
        return int(''.join(map(str,nums)))
        