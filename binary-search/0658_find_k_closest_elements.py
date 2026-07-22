"""
Problem: Find K Closest Elements
LeetCode #: 658
Difficulty: Medium
Link: https://leetcode.com/problems/find-k-closest-elements/

Approach: Binary search to find the starting index of the k-element window. Compare distance of x to arr[mid] vs arr[mid + k].
Time Complexity: O(log(n - k) + k)
Space Complexity: O(1) auxiliary space (excluding result slice)
"""

from typing import List


class Solution:
    def findClosestElements(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Check if arr[mid + k] is closer to x than arr[mid]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]
