class Solution(object):
    def missingNumber(self, nums):
        visited = set()

        for i in nums:
            visited.add(i)

        minimum_number = min(nums)
        maximum_number = max(nums)

        for i in range(minimum_number,maximum_number):
            if i not in visited:
                return i
        
        for i in range(0,minimum_number):
            return i
        
        return maximum_number + 1
        