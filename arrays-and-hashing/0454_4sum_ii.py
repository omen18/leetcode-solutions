"""
Problem: 4Sum II
LeetCode #: 454
Difficulty: Medium
Link: https://leetcode.com/problems/4sum-ii/

Approach: Count pair sums of nums1 and nums2 in a hash map, then check matching complement -(c + d) using nums3 and nums4.
Time Complexity: O(N^2) where N is length of input arrays.
Space Complexity: O(N^2) for pair sum counts map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_count = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_count[a + b] += 1

        ans = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_count:
                    ans += sum_count[target]

        return ans
