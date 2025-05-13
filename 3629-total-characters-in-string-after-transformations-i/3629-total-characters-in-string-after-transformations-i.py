class Solution(object):
    def lengthAfterTransformations(self, s, t):
        MOD = 10 ** 9 + 7
        count = [0] * 26
        res = len(s)
        z = 25
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            res = (res + count[z]) % MOD
            count[(z + 1) % 26] = (count[(z + 1) % 26] + count[z]) % MOD
            z = (z + 25) % 26
        return res


        # res = ''
        # for i in s:
        #     if i == 'z':
        #         res += 'ab'
        #     else:
        #         res += chr(ord(i) + 1)
        # if t == 1:
        #     return len(res)
        # else:
        #     return self.lengthAfterTransformations(res,t - 1)
        