class Solution:
    def reorderSpaces(self, text: str) -> str:
        words: list[str] = findall(r"(\w+)", text)
        len_words, spaces = len(words), text.count(" ")
        reorder_text: str = ""

        if len_words == 1: return words[0] + " " * spaces

        new_spaces: int = spaces // (len_words - 1)

        for index in range(len_words):
            if index == len_words - 1:
                reorder_text += words[index] + " " * ((spaces - (len_words - 1) * new_spaces))
                break
            reorder_text += words[index] + " " * new_spaces

        return reorder_text