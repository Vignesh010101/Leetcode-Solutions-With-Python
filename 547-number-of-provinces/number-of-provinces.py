class UnionFind(object):

    def __init__(self, parents: list, rank: list):
        self.parents = parents
        self.rank = rank

    def find(self, node):

        parent = node 
        while parent != self.parents[parent]:
            # don't get confused by that line
            # this is just a path compression
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def union(self, node1, node2):
        first, second = self.find(node1), self.find(node2)
        if first == second: return 0 

        if self.rank[first] > self.rank[second]:
            self.parents[second] = first
            self.rank[first] += self.rank[second]
        else:
            self.parents[first] = second
            self.rank[second] += self.rank[first]
        return 1 

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        parents = [node for node in range(len(isConnected))]
        rank = [1] * len(parents)

        unionFind = UnionFind(parents=parents, rank=rank)
        result = len(parents) 
        
        for edge1 in range(len(isConnected)):
            for otherEdge in range(len(isConnected)):
                if isConnected[edge1][otherEdge] == 1:
                    result -= unionFind.union(edge1, otherEdge)
        return result
        