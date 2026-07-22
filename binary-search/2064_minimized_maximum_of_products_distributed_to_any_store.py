"""
Problem: Minimized Maximum of Products Distributed to Any Store
LeetCode #: 2064
Difficulty: Medium
Link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

Approach: Binary search for the maximum items per store `x` in range [1, max(quantities)]. For a candidate x, count total required stores sum(ceil(q / x)). Check if stores <= n.
Time Complexity: O(m * log(max(quantities))) where m = len(quantities)
Space Complexity: O(1)
"""

import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            stores_needed = sum(math.ceil(q / mid) for q in quantities)

            if stores_needed <= n:
                right = mid
            else:
                left = mid + 1

        return left
