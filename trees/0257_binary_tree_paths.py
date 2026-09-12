"""
Problem: Binary Tree Paths
LeetCode #: 257
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-paths/

Approach: DFS preorder traversal appending node values to path string.
Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return res


if __name__ == "__main__":
    sol = Solution()
    r = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(sol.binaryTreePaths(r))  # ["1->2->5", "1->3"]
