# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        levels = {}

        def levelOrder(node, level):
            if not node:
                return
            
            if level in levels:
                levels[level][0] += node.val
                levels[level][1] += 1
            else:
                levels[level] = [node.val, 1]

            level += 1
            levelOrder(node.left, level)
            levelOrder(node.right, level)

        
        levelOrder(root, 0)

        res = []
        for v in levels.values():
            res.append(v[0]/v[1])
        
        return res