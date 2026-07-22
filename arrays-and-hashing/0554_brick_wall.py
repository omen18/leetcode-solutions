"""
Problem: Brick Wall
LeetCode #: 554
Difficulty: Medium
Link: https://leetcode.com/problems/brick-wall/

Approach: Hash map tracking counts of brick boundaries. The optimal vertical line passes through maximum boundary count.
Time Complexity: O(N) where N is total number of bricks.
Space Complexity: O(W) where W is number of unique edge positions.
"""

from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_count = defaultdict(int)

        for row in wall:
            curr_pos = 0
            for brick in row[:-1]:
                curr_pos += brick
                gap_count[curr_pos] += 1

        max_gaps = max(gap_count.values(), default=0)
        return len(wall) - max_gaps
