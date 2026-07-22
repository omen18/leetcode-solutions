"""
Problem: Max Sum of Rectangle No Larger Than K
LeetCode #: 363
Difficulty: Hard
Link: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Approach: 2D prefix sum with 1D subproblem reduction. Fix pairs of boundaries (columns or rows) to reduce to 1D max subarray sum <= k using binary search on running prefix sums.
Time Complexity: O(min(m, n)^2 * max(m, n) * log(max(m, n)))
Space Complexity: O(max(m, n))
"""

import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Ensure cols <= rows by transposing if needed to minimize outer loops
        if cols > rows:
            matrix = [list(col) for col in zip(*matrix)]
            rows, cols = cols, rows

        max_sum = float('-inf')

        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    row_sums[r] += matrix[r][right]

                # Find max 1D subarray sum <= k in row_sums
                sorted_prefix_sums = [0]
                curr_sum = 0
                for val in row_sums:
                    curr_sum += val
                    # We want curr_sum - target <= k => target >= curr_sum - k
                    idx = bisect.bisect_left(sorted_prefix_sums, curr_sum - k)
                    if idx < len(sorted_prefix_sums):
                        max_sum = max(max_sum, curr_sum - sorted_prefix_sums[idx])
                    bisect.insort(sorted_prefix_sums, curr_sum)

        return max_sum
