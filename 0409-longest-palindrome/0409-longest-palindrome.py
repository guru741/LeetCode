class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        for i in count.values():
            if i % 2 == 0:
                length += i 
            else:
                length += i - 1
                odd_found = True
        if odd_found:
            length += 1
        return length