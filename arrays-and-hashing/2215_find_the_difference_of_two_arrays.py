"""
Problem: Find the Difference of Two Arrays
LeetCode #: 2215
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/

Approach: Convert both input arrays to hash sets and compute set differences set1 - set2 and set2 - set1.
Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2.
Space Complexity: O(n + m)
"""

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
