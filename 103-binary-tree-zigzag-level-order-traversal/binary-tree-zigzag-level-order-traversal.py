# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []
    dq = collections.deque([root])
    isLeftToRight = True

    while dq:
      currLevel = []
      for _ in range(len(dq)):
        if isLeftToRight:
          node = dq.popleft()
          currLevel.append(node.val)
          if node.left:
            dq.append(node.left)
          if node.right:
            dq.append(node.right)
        else:
          node = dq.pop()
          currLevel.append(node.val)
          if node.right:
            dq.appendleft(node.right)
          if node.left:
            dq.appendleft(node.left)
      ans.append(currLevel)
      isLeftToRight = not isLeftToRight

    return ans        