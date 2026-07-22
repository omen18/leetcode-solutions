"""
Problem: Flip Columns For Maximum Number of Equal Rows
LeetCode #: 1072
Difficulty: Medium
Link: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

Approach: Two rows can become identical if they are identical or exact bitwise inverses. Normalize each row pattern starting with 0.
Time Complexity: O(M * N) where M is rows and N is columns.
Space Complexity: O(M * N) for storing row patterns in hash map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)

        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - val for val in row)
            pattern_count[pattern] += 1

        return max(pattern_count.values())
