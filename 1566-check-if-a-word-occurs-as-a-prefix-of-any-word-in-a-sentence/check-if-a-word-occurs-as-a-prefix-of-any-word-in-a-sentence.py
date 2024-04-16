class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, s in enumerate(sentence.split(" ")) :
            if s.startswith(searchWord) :
                return i + 1
        return -1