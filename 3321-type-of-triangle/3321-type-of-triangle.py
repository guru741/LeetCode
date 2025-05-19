class Solution(object):
    def triangleType(self, nums):
        a,b,c = sorted(nums)

        if(a + b) <= c or a <= 0:
            return "none"
        
        if a == c:
            return "equilateral"
        
        if a == b or b == c:
            return "isosceles"
        return "scalene"

        