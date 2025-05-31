class Solution(object):
    def kthSmallest(self, mat, k):
        n = len(mat)
        def smallest(mid):
            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if mat[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        low,high = mat[0][0],mat[n - 1][n - 1]
        while low < high:
            mid = (low + high) // 2
            if smallest(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low