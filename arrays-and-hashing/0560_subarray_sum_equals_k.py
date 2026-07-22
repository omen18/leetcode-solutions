"""
Problem: Subarray Sum Equals K
LeetCode #: 560
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Approach: Maintain prefix sums and store frequency of prefix sums in hash map. If (curr_sum - k) exists in map, add count.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for hash map storing prefix sum frequencies.
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_counts:
                count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1

        return count
