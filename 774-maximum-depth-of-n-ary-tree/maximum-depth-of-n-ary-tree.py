"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return 0
        for child in root.children:
            childDepth = self.maxDepth(child)
            depth = max(depth, childDepth)
        return depth + 1        