class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge={}
        for row in wall:
            edge_pos=0
            for brick_width in row[:-1]:
                edge_pos+=brick_width
                edge[edge_pos]=edge.get(edge_pos,0)+1

        return len(wall)-max(edge.values(), default=0)