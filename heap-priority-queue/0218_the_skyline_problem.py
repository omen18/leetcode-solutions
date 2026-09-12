"""
Problem: The Skyline Problem
LeetCode #: 218
Difficulty: Hard
Link: https://leetcode.com/problems/the-skyline-problem/

Approach: Line sweep algorithm with max-heap to track active building heights.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, neg_h, r in events:
            while live[0][1] <= pos:
                heapq.heappop(live)
            if neg_h != 0:
                heapq.heappush(live, (neg_h, r))
            curr_h = -live[0][0]
            if res[-1][1] != curr_h:
                res.append([pos, curr_h])
        return res[1:]


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15]]))
