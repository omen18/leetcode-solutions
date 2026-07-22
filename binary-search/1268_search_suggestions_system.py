"""
Problem: Search Suggestions System
LeetCode #: 1268
Difficulty: Medium
Link: https://leetcode.com/problems/search-suggestions-system/

Approach: Sort products lexicographically. For each prefix in searchWord, use binary search (bisect_left) to find the first matching product, and pick up to 3 products matching prefix.
Time Complexity: O(N log N + M log N) where N = len(products), M = len(searchWord)
Space Complexity: O(N) for sorting / storing products
"""

import bisect
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        prefix = ""
        result = []
        start_idx = 0

        for char in searchWord:
            prefix += char
            start_idx = bisect.bisect_left(products, prefix, start_idx)

            suggestions = []
            for i in range(start_idx, min(start_idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result
