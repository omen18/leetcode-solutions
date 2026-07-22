"""
Problem: Coin Change II
LeetCode #: 518
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change-ii/

Approach: Dynamic Programming unbounded knapsack counting combinations by outer looping through coins.
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]
