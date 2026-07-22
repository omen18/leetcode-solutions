"""
Problem: Sliding Window Maximum
LeetCode #: 239
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-maximum/

Approach: Monotonic decreasing deque storing indices. Maintain elements in decreasing order in deque. Remove out-of-bound indices from front.
Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices that are out of bound for the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Append front of deque (max element) to result for complete windows
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
