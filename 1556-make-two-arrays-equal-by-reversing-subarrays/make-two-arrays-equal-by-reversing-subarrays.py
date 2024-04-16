class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort(reverse=True)
        arr.sort(reverse=True)
        if target==arr:
            return True
        else:
            return False