# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = [root]
        while True:
            d1 = [y for x in d for y in [x.left, x.right] if y]
            if d1:
                d = d1
            else:
                return sum(x.val for x in d)