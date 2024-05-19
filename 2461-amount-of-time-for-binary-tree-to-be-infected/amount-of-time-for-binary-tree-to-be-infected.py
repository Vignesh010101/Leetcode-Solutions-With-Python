# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        infected = deque()
        def addParent(node, prev):
            if not node: return
            node.parent = prev
            addParent(node.left, node)
            addParent(node.right, node)

            if node.val == start: 
                infected.append(node)
        
        addParent(root, None)


        time = 0
        while infected:
            sz = len(infected)
            for i in range(sz):
                cur = infected.popleft()
                cur.val *= -1
                if cur.left and cur.left.val > 0: infected.append(cur.left)
                if cur.right and cur.right.val > 0: infected.append(cur.right)
                if cur.parent and cur.parent.val > 0: infected.append(cur.parent)
            if infected: time += 1

        return time