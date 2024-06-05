class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        S = [set() for _ in range(26)]
        for x in ideas:
            S[ord(x[0])-97].add(x[1:])
        n = 0
        for x, y in combinations(S, 2):
            a = len(x&y)
            n += (len(x)-a) * (len(y)-a)
        return n * 2