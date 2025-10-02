class Solution(object):
    def containsDuplicate(self, nums):
        ans = Counter(nums)
        for i,j in ans.items():
            if j >= 2:
                return True
        return False
        