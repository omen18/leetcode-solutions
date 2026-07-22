"""
Problem: Max Number of K-Sum Pairs
LeetCode #: 1679
Difficulty: Medium
Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/

Approach: Single pass using hash map of element frequencies. Match element with complement (k - num) if present.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for frequency map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        ops = 0

        for num in nums:
            target = k - num
            if counts[target] > 0:
                ops += 1
                counts[target] -= 1
            else:
                counts[num] += 1

        return ops
