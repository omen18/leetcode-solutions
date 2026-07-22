"""
Problem: Bitwise ORs of Subarrays
LeetCode #: 898
Difficulty: Medium
Link: https://leetcode.com/problems/bitwise-ors-of-subarrays/

Approach: Dynamic programming maintaining set of unique OR results ending at each position. Set size is bounded by 32.
Time Complexity: O(32 * N) = O(N)
Space Complexity: O(32 * N) = O(N)
"""

from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for x in arr:
            cur = {x | y for y in cur} | {x}
            res |= cur

        return len(res)
