# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node):
            if node:
                inorder(node.left)
                self.vec.append(node.val)
                inorder(node.right)

        self.vec = []
        inorder(root)

        i, j = 0, len(self.vec) - 1

        while i < j:
            curr_sum = self.vec[i] + self.vec[j]

            if curr_sum == k:
                return True
            elif curr_sum < k:
                i += 1
            elif curr_sum > k:
                j -= 1

        return False        