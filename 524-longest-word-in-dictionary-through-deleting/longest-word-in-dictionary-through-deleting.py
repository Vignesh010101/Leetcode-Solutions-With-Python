class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # Sort the dictionary by length and lexicographically
        d.sort(key=lambda x: (-len(x), x))
        
        # Traverse through the dictionary
        for word in d:
            i = 0
            # Traverse through the string s
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
                    # If we have found all the characters in the word, break the loop
                    if i == len(word):
                        break
            # If we have found all the characters in the word, return the word
            if i == len(word):
                return word
        return ""