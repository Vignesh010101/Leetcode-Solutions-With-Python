# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    newRoot = None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.DFS(root)
        return self.newRoot

    def DFS(self, root: TreeNode) -> None:
        if not root:
            return
        self.DFS(root.right)
        self.newRoot = TreeNode(root.val, None, self.newRoot)
        self.DFS(root.left)