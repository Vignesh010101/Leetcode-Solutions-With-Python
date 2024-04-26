class Solution:
    def findMaxLength(self, a: List[int]) -> int:
        return (c:={0:-1},q:=0) and max(i-c.setdefault(q:=q+v-.5,i) for i,v in enumerate(a))