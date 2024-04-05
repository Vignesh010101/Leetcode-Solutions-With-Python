"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr=[]
        def ordr(root):
            if root is None: return None
            for i in root.children:
                ordr(i)
            arr.append(root.val)
        ordr(root)
        return arr