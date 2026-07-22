"""
Problem: Maximum Performance of a Team
LeetCode #: 1383
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-performance-of-a-team/

Approach: Pair engineer speeds and efficiencies, and sort in descending order of efficiency.
Iterate through the sorted engineers, adding their speeds to a min-heap to keep track of the top k speeds seen so far.
Maintain `speed_sum`. If min-heap size exceeds k, pop the smallest speed and subtract it from `speed_sum`.
At each step, calculate `performance = speed_sum * current_efficiency` and track maximum performance.

Time Complexity: O(N log N + N log k)
Space Complexity: O(N + k)
"""

import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        min_heap = []
        speed_sum = 0
        max_perf = 0

        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            speed_sum += spd

            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)

            max_perf = max(max_perf, speed_sum * eff)

        return max_perf % (10**9 + 7)
