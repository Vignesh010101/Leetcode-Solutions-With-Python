class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                result[i] += 1

            if stack:
                result[i] += 1

            stack.append(heights[i])

        return result