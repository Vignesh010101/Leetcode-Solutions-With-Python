class Solution:
    # Function to check if characters in words can be rearranged
    # to make each word have the same characters in the same frequency.
    def makeEqual(self, words):
        # Array to store the count of each character (initialized to 0).
        characterCount = [0] * 26

        # Loop through each word in the input array 'words'.
        for inputWord in words:
            # Loop through each character in the current word.
            for inputChar in inputWord:
                # Increment the count of the current character in 'characterCount'.
                characterCount[ord(inputChar) - ord('a')] += 1

        # Check if the count of each character is divisible by the total number of words.
        for count in characterCount:
            if count % len(words) != 0:
                # If not divisible, characters cannot be rearranged to make all words equal.
                return False

        # If all characters can be rearranged to make words equal, return True.
        return True