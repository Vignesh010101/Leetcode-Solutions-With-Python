# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaves(tree):
            if tree == None:
                return []
            elif tree.left == tree.right == None:
                return [tree.val]
            else:
                return find_leaves(tree.left) + find_leaves(tree.right)
        return find_leaves(root1) == find_leaves(root2)  