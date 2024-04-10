
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()  # Split the text into words.
        ans = []  # List to hold the answers.

        # Iterate through words, stopping before the last two to avoid index errors.
        for i in range(len(words) - 2):
            # If the current word and the next word match `first` and `second`, add the third word.
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])

        return ans
        