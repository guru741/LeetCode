class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        count = 0
        for i in range(len(timeSeries) - 1):
            ans = timeSeries[i + 1] - timeSeries[i]
            count += min(duration,ans)
        return count + duration
        