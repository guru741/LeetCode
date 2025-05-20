class Solution(object):
    def searchMatrix(self, mat, target):
        for i in range(len(mat)):
            st ,end = 0,len(mat[0]) - 1 
            while st <= end:
                mid = (st + end) // 2
                if mat[i][mid] == target:
                    return True
                elif mat[i][mid] < target:
                    st = mid + 1
                else:
                    end = mid - 1
        
        return False
        