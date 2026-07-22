"""
Problem: Champagne Tower
LeetCode #: 799
Difficulty: Medium
Link: https://leetcode.com/problems/champagne-tower/

Approach: Dynamic Programming / Simulation. Simulate liquid flowing down row by row.
Start with `poured` in row 0, glass 0. For each glass with amount > 1, pass `(amount - 1) / 2` to the two
glasses directly below it in the next row. Stop at `query_row` and cap the result at 1.0.
Time Complexity: O(R^2) where R is query_row
Space Complexity: O(R)
"""

from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for r in range(query_row):
            next_row = [0.0] * (len(row) + 1)
            for c in range(len(row)):
                excess = (row[c] - 1.0) / 2.0
                if excess > 0:
                    next_row[c] += excess
                    next_row[c + 1] += excess
            row = next_row
        return min(1.0, row[query_glass])
