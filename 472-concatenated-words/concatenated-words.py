class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Create a set of all words in the given list
        wordSet = set(words)

        # Define a recursive function to check if a word is concatenated
        @functools.lru_cache(None)  # Memoize the function with least-recently-used cache
        def isConcat(word: str) -> bool:
            for i in range(1, len(word)):  # Try all possible splits of the word
                prefix = word[:i]  # Get the prefix of the split
                suffix = word[i:]  # Get the suffix of the split
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    # If the prefix is in the wordSet and the suffix is either in the wordSet
                    # or can be formed by concatenating other words, then the word is
                    # concatenated
                    return True
            return False

        # Use a list comprehension to get all concatenated words
        return [word for word in words if isConcat(word)]