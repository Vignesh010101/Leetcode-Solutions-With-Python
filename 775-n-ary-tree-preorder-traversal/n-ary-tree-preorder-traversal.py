"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        # To store the output result...
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        # Base case: If root is none...
        if root is None: return
        # Append the value of the root node to the output...
        output.append(root.val)
        # Recursively traverse each node in the children array...
        for child in root.children:
            self.traverse(child, output)        