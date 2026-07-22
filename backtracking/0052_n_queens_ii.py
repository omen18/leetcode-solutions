"""
Problem: N-Queens II
LeetCode #: 52
Difficulty: Hard
Link: https://leetcode.com/problems/n-queens-ii/

Approach: Backtracking with Bitwise Operations. Track occupied columns, main diagonals, and anti-diagonals using integer bitmasks for maximum efficiency.
Time Complexity: O(N!)
Space Complexity: O(N) for recursion stack depth.
"""

from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        
        def backtrack(r: int, cols: int, pos_diag: int, neg_diag: int) -> None:
            nonlocal count
            if r == n:
                count += 1
                return
            
            available = ((1 << n) - 1) & ~(cols | pos_diag | neg_diag)
            
            while available:
                position = available & -available
                available &= available - 1
                backtrack(
                    r + 1,
                    cols | position,
                    (pos_diag | position) << 1,
                    (neg_diag | position) >> 1
                )
                
        backtrack(0, 0, 0, 0)
        return count
