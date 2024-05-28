class Solution:
    def minimumTime(self, s: str) -> int:
        length, start, res = len(s), 0, len(s)
        for i, c in enumerate(s):
            start = min(start + (c == "1") * 2, i + 1)
            res = min(res, start + length - 1 - i)
        return res