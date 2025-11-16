class Solution(object):
    def numSub(self, s):
        mod = 10 ** 9 + 7
        count,total = 0,0
        for i in s:
            if i == '1':
                count += 1
            else:
                if count:
                    total = (total + count * (count + 1) // 2) % mod
                    count = 0
        if count:
            total = (total + count * (count + 1) // 2) % mod
        return total
        