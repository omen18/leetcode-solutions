"""
Problem: Find K Pairs with Smallest Sums
LeetCode #: 373
Difficulty: Medium
Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Approach: Use a min-heap to keep track of pair sums.
Initialize min-heap with (nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1))).
Pop the minimum element (sum, i, j), add [nums1[i], nums2[j]] to result.
If j + 1 < len(nums2), push (nums1[i] + nums2[j+1], i, j+1) to heap. Repeat k times or until heap is empty.

Time Complexity: O(k log min(k, N)) where N is len(nums1)
Space Complexity: O(min(k, N))
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or k <= 0:
            return res

        min_heap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(res) < k:
            val, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
