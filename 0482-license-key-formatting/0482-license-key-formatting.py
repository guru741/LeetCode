class Solution(object):
    def licenseKeyFormatting(self, s, k):
        res = s.replace('-','').upper()
        ans = []
        first = len(res) % k
        if first:
            ans.append(res[:first])
        for i in range(first,len(res),k):
            ans.append(res[i : i + k])
        return '-'.join(ans)
        