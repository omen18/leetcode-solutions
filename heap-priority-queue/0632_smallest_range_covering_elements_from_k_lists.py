"""
Problem: Smallest Range Covering Elements from K Lists
LeetCode #: 632
Difficulty: Hard
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

Approach: Maintain a Min-Heap storing (val, r, c) initialized with the first element of each list r.
Track `current_max` among all elements currently in the heap.
At each step:
  - Pop min element (min_val, r, c).
  - Update `best_range` if `current_max - min_val` is smaller than current best range size.
  - If c + 1 < len(nums[r]), push (nums[r][c+1], r, c+1) and update `current_max = max(current_max, nums[r][c+1])`.
  - If c + 1 == len(nums[r]), we can no longer cover all k lists, stop loop.

Time Complexity: O(N log K) where N is total elements across all K lists
Space Complexity: O(K)
"""

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')

        for r in range(len(nums)):
            val = nums[r][0]
            heapq.heappush(min_heap, (val, r, 0))
            current_max = max(current_max, val)

        res = [float('-inf'), float('inf')]

        while min_heap:
            min_val, r, c = heapq.heappop(min_heap)

            if current_max - min_val < res[1] - res[0]:
                res = [min_val, current_max]

            if c + 1 < len(nums[r]):
                next_val = nums[r][c + 1]
                heapq.heappush(min_heap, (next_val, r, c + 1))
                current_max = max(current_max, next_val)
            else:
                break

        return res
