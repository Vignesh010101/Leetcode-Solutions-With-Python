# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
    ans = []

    def dfs(root: TreeNode, summ: int, path: List[int]) -> None:
      if not root:
        return
      if root.val == summ and not root.left and not root.right:
        ans.append(path + [root.val])
        return

      dfs(root.left, summ - root.val, path + [root.val])
      dfs(root.right, summ - root.val, path + [root.val])

    dfs(root, summ, [])
    return ans