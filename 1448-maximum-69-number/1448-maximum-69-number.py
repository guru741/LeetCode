class Solution(object):
    def maximum69Number (self, num):
        l = list(str(num))

        for i in range(len(l)):
            if l[i] == '6':
                l[i] = '9'
                break
        return int("".join(l))
        