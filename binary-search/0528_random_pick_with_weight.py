"""
Problem: Random Pick with Weight
LeetCode #: 528
Difficulty: Medium
Link: https://leetcode.com/problems/random-pick-with-weight/

Approach: Compute prefix sums of weights. Generate a random target in range [1, total_sum] and use binary search (bisect_left) on prefix sums to find index.
Time Complexity: __init__: O(n), pickIndex: O(log n)
Space Complexity: O(n)
"""

import bisect
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix_sums, target)
