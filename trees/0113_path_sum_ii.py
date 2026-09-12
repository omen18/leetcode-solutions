"""
Problem: Path Sum II
LeetCode #: 113
Difficulty: Medium
Link: https://leetcode.com/problems/path-sum-ii/

Approach: DFS backtracking collecting all root-to-leaf paths equaling target sum.
Time Complexity: O(n^2)
Space Complexity: O(h)
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, curr_sum, path):
            if not node:
                return
            path.append(node.val)
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(list(path))
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)
            path.pop()

        dfs(root, 0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
    print(sol.pathSum(root, 22))  # [[5, 4, 11, 2]]
