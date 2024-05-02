# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        ## Diameter of binary tree concept 
        #  https://leetcode.com/problems/diameter-of-binary-tree/description/
        def dfs(node, parent):
            if not node:
                return 0
            
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            
            ## The longest path will cover nodes on both sides of the root. 
            self.ans = max(self.ans, left+right)

            ## if the node doesn't equal it's parent, we return 0, otherwise we add left, right +1 (for root)
            if parent and node.val == parent.val: # to check if child path matches the root, otherwise that child will return 0
                return max(left, right)+1
            return 0
            
        print(dfs(root, None))
        return self.ans

        