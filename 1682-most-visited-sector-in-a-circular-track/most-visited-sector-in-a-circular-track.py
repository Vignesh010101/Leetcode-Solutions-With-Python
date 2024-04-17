class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        x, xx = rounds[0], rounds[-1]
        return list(range(x, xx+1)) if x <= xx else list(range(1, xx+1)) + list(range(x, n+1))