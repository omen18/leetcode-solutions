"""
Problem: Minimize Deviation in Array
LeetCode #: 1675
Difficulty: Hard
Link: https://leetcode.com/problems/minimize-deviation-in-array/

Approach: Transform all odd numbers to even (multiply by 2) so all elements are at their maximum possible value.
Insert all numbers into a Max-Heap (as negated values) and track `current_min`.
In each step:
  - Pop max value from heap. Update min deviation: `min_dev = min(min_dev, max_val - current_min)`.
  - If `max_val` is even, divide by 2, push back to heap, and update `current_min = min(current_min, max_val // 2)`.
  - If `max_val` is odd, it cannot be reduced further, stop loop.

Time Complexity: O(N log N log M) where M is max value in nums
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        current_min = float('inf')

        for n in nums:
            if n % 2 != 0:
                n *= 2
            heapq.heappush(max_heap, -n)
            current_min = min(current_min, n)

        min_dev = float('inf')

        while max_heap:
            max_val = -heapq.heappop(max_heap)
            min_dev = min(min_dev, max_val - current_min)

            if max_val % 2 == 0:
                new_val = max_val // 2
                heapq.heappush(max_heap, -new_val)
                current_min = min(current_min, new_val)
            else:
                break

        return min_dev
