class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom,maga = Counter(ransomNote),Counter(magazine)
        return not(ransom - maga)
        