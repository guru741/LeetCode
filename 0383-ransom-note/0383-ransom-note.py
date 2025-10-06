class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # ransom,maga = Counter(ransomNote),Counter(magazine)
        # return not(ransom - maga)
        freq = [0] * 26
        for i in magazine:
            freq[ord(i) - ord('a')] += 1
        for i in ransomNote:
            freq[ord(i) - ord('a')] -= 1
            if freq[ord(i) - ord('a')] < 0:
                return False
        return True