"""
Problem: Remove Boxes
LeetCode #: 546
Difficulty: Hard
Link: https://leetcode.com/problems/remove-boxes/

Approach: 3D Dynamic Programming with Memoization.
`dp(i, j, k)` represents the maximum points obtainable from substring `boxes[i..j]` given that there are `k` boxes
preceding index `i` with the exact same color as `boxes[i]`.
Two transition choices:
1. Remove `boxes[i]` together with the `k` preceding matching boxes: `(k + 1)^2 + dp(i + 1, j, 0)`.
2. Find index `m` in `[i+1..j]` where `boxes[m] == boxes[i]` and combine them: `dp(i + 1, m - 1, 0) + dp(m, j, k + 1)`.
Time Complexity: O(N^4) upper bound, O(N^3) practical
Space Complexity: O(N^3)
"""

from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0

            # Optimize contiguous duplicate boxes at start of subarray
            while i + 1 <= j and boxes[i + 1] == boxes[i]:
                i += 1
                k += 1

            # Option 1: Remove boxes[i] along with k matching boxes
            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)

            # Option 2: Merge boxes[i] with boxes[m] of the same color
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

            return res

        return dp(0, n - 1, 0)
