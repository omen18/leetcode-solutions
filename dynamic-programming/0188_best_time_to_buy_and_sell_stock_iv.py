"""
Problem: Best Time to Buy and Sell Stock IV
LeetCode #: 188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Approach: Dynamic Programming. If `k >= n // 2`, solve using greedy stock trading with unlimited transactions.
Otherwise, maintain `buy` and `sell` state arrays of size `k + 1`. For each price:
- `buy[j] = min(buy[j], price - sell[j - 1])`
- `sell[j] = max(sell[j], price - buy[j])`
Time Complexity: O(N * K)
Space Complexity: O(K)
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Unlimited transactions edge case
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        buy = [float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = min(buy[j], price - sell[j - 1])
                sell[j] = max(sell[j], price - buy[j])

        return sell[k]
