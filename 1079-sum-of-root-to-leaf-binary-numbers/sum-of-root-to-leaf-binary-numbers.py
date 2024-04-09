# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return 0
        def dfs(node, slate):
            nonlocal result
            if not node.left and not node.right:
                slate.append(str(node.val))
                result += int("".join(slate), 2)
            
            if node.left: dfs(node.left, slate + [str(node.val)])
            if node.right: dfs(node.right, slate + [str(node.val)])
        
        dfs(root, [])
        return result