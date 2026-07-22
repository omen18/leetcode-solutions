"""
Problem: Maximum Product of Word Lengths
LeetCode #: 318
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-of-word-lengths/

Approach: Represent each word as a 26-bit integer mask. Compare masks using bitwise AND to check for shared characters.
Time Complexity: O(N * L + N^2)
Space Complexity: O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask_map = defaultdict(int)

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord("a"))
            mask_map[mask] = max(mask_map[mask], len(word))

        max_prod = 0
        masks = list(mask_map.keys())

        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                m1, m2 = masks[i], masks[j]
                if (m1 & m2) == 0:
                    max_prod = max(max_prod, mask_map[m1] * mask_map[m2])

        return max_prod
