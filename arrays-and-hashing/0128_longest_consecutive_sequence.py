"""
Problem: Longest Consecutive Sequence
LeetCode #: 128
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Approach: Insert numbers into a set. Start counting sequence length only from numbers that are sequence starts (num - 1 not in set).
Time Complexity: O(N) where N is the length of nums.
Space Complexity: O(N) to store elements in set.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                curr_len = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_len += 1
                longest = max(longest, curr_len)

        return longest
