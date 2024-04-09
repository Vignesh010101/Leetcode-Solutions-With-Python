# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def preorder(root) :
            if not root :
                return 
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        sol = 0
        for i in ans :
            if (low <= i <= high) :
                sol += i
        return sol 
        
        