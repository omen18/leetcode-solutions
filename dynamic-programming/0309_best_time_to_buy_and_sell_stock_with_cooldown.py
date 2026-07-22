"""
Problem: Best Time to Buy and Sell Stock with Cooldown
LeetCode #: 309
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Approach: State Machine DP maintaining max profits in held, sold, and cooldown/reset states.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        held = -prices[0]
        sold = 0
        reset = 0
        
        for i in range(1, len(prices)):
            prev_sold = sold
            sold = held + prices[i]
            held = max(held, reset - prices[i])
            reset = max(reset, prev_sold)
            
        return max(sold, reset)
