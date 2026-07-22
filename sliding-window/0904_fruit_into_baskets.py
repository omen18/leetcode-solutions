"""
Problem: Fruit Into Baskets
LeetCode #: 904
Difficulty: Medium
Link: https://leetcode.com/problems/fruit-into-baskets/

Approach: Find longest subarray with at most 2 distinct elements. Sliding window using frequency hash map. Shrink left when map size > 2.
Time Complexity: O(n)
Space Complexity: O(1) (at most 3 distinct entries in map)
"""

from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
