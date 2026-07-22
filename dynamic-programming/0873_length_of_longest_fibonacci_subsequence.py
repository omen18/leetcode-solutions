"""
Problem: Length of Longest Fibonacci Subsequence
LeetCode #: 873
Difficulty: Medium
Link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

Approach: Dynamic Programming with Hash Map. Map each value in `arr` to its index. `dp[(j, i)]` stores the length
of the longest Fibonacci-like subsequence ending at indices `j` and `i` (`j < i`). For pair `(j, i)`, check if
`diff = arr[i] - arr[j]` exists at index `k < j`. If so, `dp[(j, i)] = dp[(k, j)] + 1`.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {val: i for i, val in enumerate(arr)}
        dp = {}
        max_len = 0

        for i in range(len(arr)):
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in index_map and index_map[diff] < j:
                    k = index_map[diff]
                    dp[j, i] = dp.get((k, j), 2) + 1
                    max_len = max(max_len, dp[j, i])

        return max_len if max_len >= 3 else 0
