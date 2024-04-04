# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def get_sum(root):
            return root.val + get_sum(root.left) + get_sum(root.right) if root else 0
        
        def helper(root):
            global ans
            if root is None:
                return 0
            else:
                ans+= abs(get_sum(root.left) - get_sum(root.right))
                helper(root.left)
                helper(root.right)
                return ans
                
        global ans
        ans=0
        helper(root)
        return ans