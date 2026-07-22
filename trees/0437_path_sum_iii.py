"""
Problem: Path Sum III
LeetCode #: 437
Difficulty: Medium
Link: https://leetcode.com/problems/path-sum-iii/

Approach: Prefix sum array with hash map & backtracking DFS. Track running prefix sum from root to current node. If (current_sum - targetSum) exists in hash map, add its frequency to total path count.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for hash map storing prefix sums.
"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums[current_sum - targetSum]

            prefix_sums[current_sum] += 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1

            return count

        return dfs(root, 0)
