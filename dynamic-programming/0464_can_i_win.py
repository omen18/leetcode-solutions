"""
Problem: Can I Win
LeetCode #: 464
Difficulty: Medium
Link: https://leetcode.com/problems/can-i-win/

Approach: Top-down Minimax DP with Bitmask Memoization tracking used integers.
Time Complexity: O(2^M * M) where M is maxChoosableInteger
Space Complexity: O(2^M)
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
            
        memo = {}
        
        def can_win(used_mask: int, current_total: int) -> bool:
            if used_mask in memo:
                return memo[used_mask]
                
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i
                if not (used_mask & bit):
                    if current_total + i >= desiredTotal or not can_win(used_mask | bit, current_total + i):
                        memo[used_mask] = True
                        return True
                        
            memo[used_mask] = False
            return False
            
        return can_win(0, 0)
