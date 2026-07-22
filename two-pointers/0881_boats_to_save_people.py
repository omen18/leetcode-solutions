"""
Problem: Boats to Save People
LeetCode #: 881
Difficulty: Medium
Link: https://leetcode.com/problems/boats-to-save-people/

Approach: Sort weights. Use two pointers (`left` for lightest, `right` for heaviest). If `people[left] + people[right] <= limit`, pair them in one boat. Otherwise, heaviest goes alone.
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary (excluding sorting)
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if left != right and people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats
