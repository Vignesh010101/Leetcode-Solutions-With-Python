# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])

    while q:
      size = len(q)
      for i in range(size):
        root = q.popleft()
        if i == size - 1:
          ans.append(root.val)
        if root.left:
          q.append(root.left)
        if root.right:
          q.append(root.right)

    return ans        