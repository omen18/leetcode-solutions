"""
Problem: Count Good Nodes in Binary Tree
LeetCode #: 1448
Difficulty: Medium
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Approach: DFS tracking maximum value on path from root to current node. Node is 'good' if its value is >= max_val. Update max_val and recurse to children.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(H) where H is height of the tree for recursion stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0

            count = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)
