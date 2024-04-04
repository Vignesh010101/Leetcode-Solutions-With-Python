# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it means any subtree can match, so return True
        if subRoot == None :
            return True

        # If root is None, there are no nodes left in the root tree to check, so return False
        if root == None :
            return False

        # If the subtree rooted at the current node of root matches the subRoot, return True
        if self.same(root , subRoot):
            return True
        
        # Recursively check if subRoot is a subtree of the left or right child of the current node
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

    # Helper function to check if two subtrees are identical
    def same(self , r , s):
        # If both trees are None, they are identical
        if r == None and s == None :
            return True

        # If one tree is None while the other is not, they are not identical
        if r and s and r.val == s.val:
            # Recursively check if the left and right subtrees are identical
            return self.same(r.right , s.right) and self.same(r.left , s.left)  

        # If the values of the current nodes do not match, the trees are not identical
        return False  