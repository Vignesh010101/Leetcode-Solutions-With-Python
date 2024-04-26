# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        stack, summ, node = [], 0, root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += summ
            summ = node.val
            node = node.left
        return root        