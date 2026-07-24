/*
 * Problem: Invert Binary Tree
 * LeetCode #: 226
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/invert-binary-tree/
 *
 * Approach: Recursive depth-first traversal swapping left and right subtrees.
 * Time Complexity: O(n)
 * Space Complexity: O(h) where h is height of tree
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);
        return root;
    }
}
