class Solution(object):
    def findKthLargest(self, arr, k):
        min_heap = [i for i in arr[:k]]
        heapq.heapify(min_heap)

        for i in range(k,len(arr)):
            if arr[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,arr[i])
        return min_heap[0]
        