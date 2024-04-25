# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        queue = [root]
        output = []
        while queue:
            current = queue.pop(0)
            if current:
                output.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append("null")
        return ",".join(output)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while queue:
            current = queue.pop(0)
            if data[i] != "null":
                current.left = TreeNode(int(data[i]))
                queue.append(current.left)
            i += 1
            if data[i] != "null":
                current.right = TreeNode(int(data[i]))
                queue.append(current.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans