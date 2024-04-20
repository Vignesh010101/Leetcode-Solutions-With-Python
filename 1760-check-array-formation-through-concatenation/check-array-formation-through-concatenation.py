class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        vy={x[0]:x for x in pieces}
        return list(chain(*[vy.get(nm, []) for nm in arr]))==arr