"""
Problem: Successful Pairs of Spells and Potions
LeetCode #: 2300
Difficulty: Medium
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

Approach: Sort potions array. For each spell, calculate the minimum required potion strength ceil(success / spell) and use binary search (bisect_left) to find the number of valid potions.
Time Complexity: O(m log m + n log m) where n = len(spells), m = len(potions)
Space Complexity: O(m) for sorted potions or O(1) auxiliary space
"""

from bisect import bisect_left
import math
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion = math.ceil(success / spell)
            idx = bisect_left(potions, min_potion)
            result.append(m - idx)

        return result
