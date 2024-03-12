"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        def nodes(a,b)->None:
            if not a:
                return
            a.next=b
            nodes(a.left, a.right)
            nodes(b.left, b.right)
            nodes(a.right, b.left)
        nodes(root.left,root.right)
        return root