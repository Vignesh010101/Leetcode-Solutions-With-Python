# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        m=max(nums)
        i=nums.index(m)
        root=TreeNode(m)
        def tree(temp,left,right):
            if left:
                ml=max(left)
                varl=TreeNode(ml)
                i=left.index(ml)
                temp.left=varl
                if i+1==len(left): tree(temp.left,left[:i],[])
                else: tree(temp.left,left[:i],left[i+1:])
            if right:
                mr=max(right)
                varr=TreeNode(mr)
                i=right.index(mr)
                temp.right=varr
                if i+1==len(right): tree(temp.right,right[:i],[])
                else: tree(temp.right,right[:i],right[i+1:])
        if i+1==len(nums):
            tree(root,nums[:i],[])
        else: tree(root,nums[:i],nums[i+1:])
        return root        