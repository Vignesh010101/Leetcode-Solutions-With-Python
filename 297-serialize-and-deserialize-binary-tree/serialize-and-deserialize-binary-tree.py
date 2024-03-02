# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root: 'TreeNode') -> str:
    """Encodes a tree to a single string."""
    if not root:
      return ''

    s = ''
    q = collections.deque([root])

    while q:
      node = q.popleft()
      if node:
        s += str(node.val) + ' '
        q.append(node.left)
        q.append(node.right)
      else:
        s += 'n '

    return s

  def deserialize(self, data: str) -> 'TreeNode':
    """Decodes your encoded data to tree."""
    if not data:
      return None

    vals = data.split()
    root = TreeNode(vals[0])
    q = collections.deque([root])

    for i in range(1, len(vals), 2):
      node = q.popleft()
      if vals[i] != 'n':
        node.left = TreeNode(vals[i])
        q.append(node.left)
      if vals[i + 1] != 'n':
        node.right = TreeNode(vals[i + 1])
        q.append(node.right)

    return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))