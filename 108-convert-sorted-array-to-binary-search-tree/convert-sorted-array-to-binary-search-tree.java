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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) { return null; }
        return helper(nums, 0, nums.length - 1);
    }
    
    private TreeNode helper(int[] nums, int lo, int hi) {
        if (lo > hi) {
            return null;
        } else if (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            TreeNode node = new TreeNode(nums[mi]);
            node.left = helper(nums, lo, mi - 1);
            node.right = helper(nums, mi + 1, hi);
            return node;
        } else {
            TreeNode node = new TreeNode(nums[lo]);
            return node;
        }
    }
}