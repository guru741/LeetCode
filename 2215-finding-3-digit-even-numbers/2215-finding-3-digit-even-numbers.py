class Solution(object):
    def findEvenNumbers(self, digits):
        freq = Counter(digits)
        res = []
        for i in range(100,1000,2):
            parts = [i // 100, (i // 10) % 10,i % 10]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                res.append(i)
        return res
        