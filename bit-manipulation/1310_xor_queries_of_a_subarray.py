"""
Problem: XOR Queries of a Subarray
LeetCode #: 1310
Difficulty: Medium
Link: https://leetcode.com/problems/xor-queries-of-a-subarray/

Approach: Build a prefix XOR array to answer each range query in O(1) time.
Time Complexity: O(N + Q)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0] * (len(arr) + 1)
        for i, val in enumerate(arr):
            pref[i + 1] = pref[i] ^ val

        return [pref[r + 1] ^ pref[l] for l, r in queries]
