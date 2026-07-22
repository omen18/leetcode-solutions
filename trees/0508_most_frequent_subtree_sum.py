"""
Problem: Most Frequent Subtree Sum
LeetCode #: 508
Difficulty: Medium
Link: https://leetcode.com/problems/most-frequent-subtree-sum/

Approach: Bottom-up postorder DFS traversal to calculate subtree sums. Store sum frequencies in a Counter hash map, find the maximum frequency, and return all sums matching that maximum frequency.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for recursion stack and frequency map.
"""

from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        counts = Counter()

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            counts[subtree_sum] += 1
            return subtree_sum

        dfs(root)
        max_freq = max(counts.values())
        return [s for s, freq in counts.items() if freq == max_freq]
