class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_word,map_char = {},{}
        
        for i in range(len(words)):
            word = words[i]
            char = pattern[i]
            if word not in map_word:
                map_word[word] = i
            if char not in map_char:
                map_char[char] = i
            if map_char[char] != map_word[word]:
                return False
        return True