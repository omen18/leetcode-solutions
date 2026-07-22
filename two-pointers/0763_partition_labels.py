"""
Problem: Partition Labels
LeetCode #: 763
Difficulty: Medium
Link: https://leetcode.com/problems/partition-labels/

Approach: Map each character to its last occurrence index. Iterate through string, expanding current partition boundary `end = max(end, last[char])`. When current index reaches `end`, complete partition.
Time Complexity: O(n)
Space Complexity: O(1) (26 characters max in map)
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        start = end = 0
        res = []

        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
