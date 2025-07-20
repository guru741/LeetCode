class Solution(object):
    def kthSmallest(self, mat, k):
        n = len(mat)
        import heapq
        min_heap = []

        for i in range(min(n,k)):
            heapq.heappush(min_heap,(mat[i][0],i,0))
        
        for _ in range(k - 1):
            val,r,c = heapq.heappop(min_heap)
            
            if c + 1 < n:
                heapq.heappush(min_heap,(mat[r][c + 1],r,c + 1))
        
        return heapq.heappop(min_heap)[0]

        # def smallest(mid):
        #     count = 0
        #     row = n - 1
        #     col = 0

        #     while row >= 0 and col < n:
        #         if mat[row][col] <= mid:
        #             count += row + 1
        #             col += 1
        #         else:
        #             row -= 1
        #     return count

        # low,high = mat[0][0],mat[n - 1][n - 1]
        # while low < high:
        #     mid = (low + high) // 2
        #     if smallest(mid) < k:
        #         low = mid + 1
        #     else:
        #         high = mid
        # return low