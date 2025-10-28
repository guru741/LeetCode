class Solution(object):
    def checkRecord(self, s):
        countA = countL = 0
        for i in range(len(s)):
            if s[i] == 'A':
                countA += 1 
                countL = 0
                if countA >= 2:
                    return False
            elif s[i] == 'L':
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0
        return True
        