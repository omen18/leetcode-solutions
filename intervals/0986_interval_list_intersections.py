"""
Problem: Interval List Intersections
LeetCode #: 986
Difficulty: Medium
Link: https://leetcode.com/problems/interval-list-intersections/

Approach: Two-pointer technique comparing intervals from firstList and secondList. Advance pointer with smaller end time.
Time Complexity: O(N + M) where N and M are lengths of firstList and secondList
Space Complexity: O(N + M) for result list
"""

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                res.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res
