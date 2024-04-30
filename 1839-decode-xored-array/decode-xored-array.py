class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        vy=[first]
        for num in encoded:
            vy.append(vy[-1]^num)
        return vy