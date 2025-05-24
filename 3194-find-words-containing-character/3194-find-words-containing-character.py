class Solution(object):
    def findWordsContaining(self, words, x):
        res = set()
        count = 0
        for word in words:
            if x in word:
                res.add(count)
            count += 1
        return list(res) if len(res) != 0 else []

        