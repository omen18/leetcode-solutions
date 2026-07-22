"""
Problem: Sliding Window Median
LeetCode #: 480
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-median/

Approach: Two heaps (max-heap for lower half, min-heap for upper half) with lazy deletion hash table for elements leaving the window. Rebalance heaps to maintain size invariant.
Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from typing import List
import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # max-heap (invert values)
        large = []  # min-heap
        delayed = Counter()

        small_size = 0
        large_size = 0

        def prune(heap, is_small):
            nonlocal small_size, large_size
            while heap:
                num = -heap[0] if is_small else heap[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                small_size -= 1
                large_size += 1
                prune(small, True)
            elif small_size < large_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                large_size -= 1
                small_size += 1
                prune(large, False)

        for i in range(k):
            heapq.heappush(small, -nums[i])
            small_size += 1

        for _ in range(k // 2):
            val = -heapq.heappop(small)
            heapq.heappush(large, val)
            small_size -= 1
            large_size += 1

        medians = []

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        medians.append(get_median())

        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]
            delayed[out_num] += 1

            if out_num <= -small[0]:
                small_size -= 1
                if out_num == -small[0]:
                    prune(small, True)
            else:
                large_size -= 1
                if large and out_num == large[0]:
                    prune(large, False)

            if small and in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                small_size += 1
            else:
                heapq.heappush(large, in_num)
                large_size += 1

            rebalance()
            medians.append(get_median())

        return medians
