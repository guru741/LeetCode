class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        left,right = 2,num // 2

        while left <= right:
            mid = left + (right - left) // 2

            decision = mid * mid

            if decision == num:
                return True
            elif decision < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        