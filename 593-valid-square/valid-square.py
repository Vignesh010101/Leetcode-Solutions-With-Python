class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1,p2):
            diffy=p2[1]-p1[1]
            diffy*=diffy
            diffx=p2[0]-p1[0]
            diffx*=diffx
            diffx+=diffy
            return math.sqrt(diffx)

        if p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4:
            return False

        return len(set([distance(p1,p2),distance(p1,p3),distance(p1,p4),distance(p2,p3),distance(p2,p4),distance(p3,p4)]))==2