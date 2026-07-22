"""
Problem: Kth Largest Element in an Array
LeetCode #: 215
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Approach: Use a min-heap of size k to maintain the k largest elements seen so far.
Iterate through the array, pushing each element to the heap. If the size exceeds k,
pop the smallest element. At the end, the top of the min-heap will be the kth largest element.

Time Complexity: O(N log k)
Space Complexity: O(k)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
