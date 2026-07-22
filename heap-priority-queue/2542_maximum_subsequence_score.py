"""
Problem: Maximum Subsequence Score
LeetCode #: 2542
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subsequence-score/

Approach: Zip nums2 and nums1 together as pairs (nums2[i], nums1[i]) and sort in descending order of nums2[i].
Maintain a Min-Heap of size k for nums1 values to keep the largest k values of nums1 seen so far.
As we iterate through the sorted pairs, nums2[i] is guaranteed to be the minimum nums2 value in the current subsequence of size k.
Track `nums1_sum`. When min-heap size reaches k, update `max_score = max(max_score, nums1_sum * nums2[i])`.

Time Complexity: O(N log N)
Space Complexity: O(N + k)
"""

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        min_heap = []
        nums1_sum = 0
        max_score = 0

        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            nums1_sum += n1

            if len(min_heap) > k:
                nums1_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, nums1_sum * n2)

        return max_score
