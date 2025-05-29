class Solution(object):
    def searchRange(self, nums, target):
        def findFirst():
            st,end,first = 0,len(nums) - 1, -1
            while st <= end:
                mid = (st + end) // 2
                if target > nums[mid]:
                    st = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    first = mid
                    end = mid - 1
            return first

        def findLast():
            st,end,last = 0,len(nums) - 1, -1
            while st <= end:
                mid = (st + end) // 2
                if target > nums[mid]:
                    st = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    last = mid
                    st = mid + 1
            return last
        return [findFirst(),findLast()]
        
        