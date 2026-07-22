"""
Problem: Maximum Value of K Coins From Piles
LeetCode #: 2218
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

Approach: 1D Dynamic Programming (Knapsack Variant) - Process each pile using prefix sums and update maximum value for each coin count.
Time Complexity: O(K * sum(len(pile)))
Space Complexity: O(K)
"""

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        
        for pile in piles:
            # We only need prefix sums up to min(len(pile), k)
            n_coins = len(pile)
            pref = [0] * (n_coins + 1)
            for i in range(n_coins):
                pref[i + 1] = pref[i] + pile[i]
                
            # Update DP array backwards
            for coins in range(k, -1, -1):
                for take in range(1, min(n_coins, coins) + 1):
                    dp[coins] = max(dp[coins], dp[coins - take] + pref[take])
                    
        return dp[k]
