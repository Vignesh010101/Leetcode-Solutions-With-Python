class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = 0
        prev = None
        intervals = []
        s = s + str(ord(s[-1]) + 1)
        for i, c in enumerate(s):
            if c != prev:
                if count >= 3:
                    intervals.append([i - count, i - 1])
                count = 1
            else:
                count += 1
            prev = c
        return intervals