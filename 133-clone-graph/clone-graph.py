"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None

    q = collections.deque([node])
    map = {node: Node(node.val)}

    while q:
      u = q.popleft()
      for v in u.neighbors:
        if v not in map:
          map[v] = Node(v.val)
          q.append(v)
        map[u].neighbors.append(map[v])

    return map[node]