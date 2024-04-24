class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        
        def helper(grid, i, j, w):
            if allSame(grid, i, j, w):
                return Node(grid[i][j] == 1, True)

            node = Node(True, False)
            node.topLeft = helper(grid, i, j, w // 2)
            node.topRight = helper(grid, i, j + w // 2, w // 2)
            node.bottomLeft = helper(grid, i + w // 2, j, w // 2)
            node.bottomRight = helper(grid, i + w // 2, j + w // 2, w // 2)
            return node

        def allSame(grid, i, j, w):
            for x in range(i, i + w):
                for y in range(j, j + w):
                    if grid[x][y] != grid[i][j]:
                        return False
            return True

        return helper(grid, 0, 0, len(grid))