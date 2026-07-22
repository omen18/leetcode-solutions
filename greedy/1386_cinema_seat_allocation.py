"""
Problem: Cinema Seat Allocation
LeetCode #: 1386
Difficulty: Medium
Link: https://leetcode.com/problems/cinema-seat-allocation/

Approach: Use bitmasks for seats 2 through 9 in each row. Unreserved rows take 2 groups. Reserved rows check left (2-5), right (6-9), or middle (4-7) blocks.
Time Complexity: O(R) where R is the number of reserved seats
Space Complexity: O(R)
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                rows[row] |= (1 << (col - 2))
                
        res = (n - len(rows)) * 2
        
        for mask in rows.values():
            left = (mask & 15) == 0
            right = (mask & 240) == 0
            middle = (mask & 60) == 0
            
            if left and right:
                res += 2
            elif left or right or middle:
                res += 1
                
        return res
