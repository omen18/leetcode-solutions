"""
Problem: K-diff Pairs in an Array
LeetCode #: 532
Difficulty: Medium
Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/

Approach: Use a frequency map (Counter). If k == 0, count elements with frequency >= 2. If k > 0, check if (x + k) exists in keys for each key x in the map.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counts = Counter(nums)
        pairs = 0

        if k == 0:
            for num, freq in counts.items():
                if freq > 1:
                    pairs += 1
        else:
            for num in counts:
                if num + k in counts:
                    pairs += 1

        return pairs
