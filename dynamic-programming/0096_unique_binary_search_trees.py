"""
Problem: Unique Binary Search Trees
LeetCode #: 96
Difficulty: Medium
Link: https://leetcode.com/problems/unique-binary-search-trees/

Approach: Dynamic Programming (Catalan numbers) - dp[i] represents number of unique BSTs with i nodes.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]
