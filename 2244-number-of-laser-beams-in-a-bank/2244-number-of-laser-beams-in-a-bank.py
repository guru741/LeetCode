class Solution(object):
    def numberOfBeams(self, bank):
        ans,res = 0,0
        for i in range(len(bank)):
            count = 0
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    count += 1
            ans += count * res
            if count != 0:
                res = count
            count = 0
        return ans
        