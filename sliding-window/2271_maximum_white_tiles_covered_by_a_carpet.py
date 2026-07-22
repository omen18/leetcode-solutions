"""
Problem: Maximum White Tiles Covered by a Carpet
LeetCode #: 2271
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

Approach: Sort tiles intervals. It is optimal to start the carpet at the beginning of a tile interval. Use a sliding window to find how many full and partial tile intervals are covered when placing carpet at `tiles[i][0]`.
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary (excluding sorting)
"""

from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        n = len(tiles)
        max_covered = 0
        current_cover = 0
        j = 0

        for i in range(n):
            carpet_start = tiles[i][0]
            carpet_end = carpet_start + carpetLen - 1

            while j < n and tiles[j][1] <= carpet_end:
                current_cover += tiles[j][1] - tiles[j][0] + 1
                j += 1

            if j < n and tiles[j][0] <= carpet_end:
                partial = carpet_end - tiles[j][0] + 1
                max_covered = max(max_covered, current_cover + partial)
            else:
                max_covered = max(max_covered, current_cover)

            current_cover -= tiles[i][1] - tiles[i][0] + 1

        return max_covered
