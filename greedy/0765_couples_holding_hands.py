"""
Problem: Couples Holding Hands
LeetCode #: 765
Difficulty: Hard
Link: https://leetcode.com/problems/couples-holding-hands/

Approach: Iterate across paired seats (0,1), (2,3), etc. For person at 2*i, locate their partner (person ^ 1) using position map and swap partner to seat 2*i+1 if necessary.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pos = {val: i for i, val in enumerate(row)}
        swaps = 0
        
        for i in range(0, n, 2):
            first = row[i]
            second = first ^ 1
            if row[i + 1] != second:
                swaps += 1
                second_pos = pos[second]
                
                # Swap row[i+1] and row[second_pos]
                row[second_pos] = row[i + 1]
                pos[row[i + 1]] = second_pos
                
                row[i + 1] = second
                pos[second] = i + 1
                
        return swaps
