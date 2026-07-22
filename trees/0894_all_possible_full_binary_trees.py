"""
Problem: All Possible Full Binary Trees
LeetCode #: 894
Difficulty: Medium
Link: https://leetcode.com/problems/all-possible-full-binary-trees/

Approach: Memoized Recursion / Dynamic Programming. A full binary tree (FBT) with N nodes exists only when N is odd. Split N-1 remaining nodes between left subtree (size L, where L is odd) and right subtree (size N-1-L, also odd).
Time Complexity: O(2^(N/2)) / Catalan number bounds.
Space Complexity: O(2^(N/2)) for memoization cache.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = {}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        if n in self.memo:
            return self.memo[n]

        result = []
        for left_size in range(1, n, 2):
            right_size = n - 1 - left_size
            left_trees = self.allPossibleFBT(left_size)
            right_trees = self.allPossibleFBT(right_size)

            for l_tree in left_trees:
                for r_tree in right_trees:
                    root = TreeNode(0)
                    root.left = l_tree
                    root.right = r_tree
                    result.append(root)

        self.memo[n] = result
        return result
