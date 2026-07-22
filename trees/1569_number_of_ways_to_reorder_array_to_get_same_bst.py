"""
Problem: Number of Ways to Reorder Array to Get Same BST
LeetCode #: 1569
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

Approach: Divide and conquer using combinatorics. The root must be the first element.
Left subtree nodes and right subtree nodes retain their relative orders internally.
The number of ways to interleave left nodes (size L) and right nodes (size R) is C(L+R, L).
Recursively compute for left and right subtrees and subtract 1 for the initial ordering.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

import math
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = dfs(left)
            right_ways = dfs(right)

            return (math.comb(len(left) + len(right), len(left)) * left_ways * right_ways) % MOD

        return (dfs(nums) - 1) % MOD
