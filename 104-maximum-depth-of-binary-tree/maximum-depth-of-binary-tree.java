/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) { return 0; }
        int depth = 0;
        LinkedList<TreeNode> list = new LinkedList<>();
        list.offer(root);
        while (!list.isEmpty()) {
            depth += 1;
            int size = list.size();
            while (size > 0) {
                TreeNode n = list.poll();
                if (n.left != null) { list.offer(n.left); }
                if (n.right != null) { list.offer(n.right); }
                size -= 1;
            }
        }
        return depth;
    }
}