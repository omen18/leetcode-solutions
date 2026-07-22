"""
Problem: Coin Change
LeetCode #: 322
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Approach: Unbounded Knapsack Dynamic Programming computing minimum coins for each value up to amount.
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1
