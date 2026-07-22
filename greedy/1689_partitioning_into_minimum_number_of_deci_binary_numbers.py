"""
Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
LeetCode #: 1689
Difficulty: Medium
Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

Approach: The minimum number of deci-binary numbers required is equal to the maximum digit present in string n.
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
