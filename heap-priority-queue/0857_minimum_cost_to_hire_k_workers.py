"""
Problem: Minimum Cost to Hire K Workers
LeetCode #: 857
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

Approach: Sort workers by wage-to-quality ratio (wage[i] / quality[i]).
Maintain a Max-Heap of worker qualities to keep the k smallest qualities among workers evaluated so far.
Maintain `quality_sum`. For each worker ratio:
  - Add worker quality to max-heap and update `quality_sum`.
  - If max-heap size exceeds k, pop maximum quality worker and subtract from `quality_sum`.
  - When max-heap size == k, total cost is `quality_sum * current_ratio`. Track min total cost.

Time Complexity: O(N log N + N log k)
Space Complexity: O(N + k)
"""

import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        max_heap = []
        quality_sum = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, quality_sum * ratio)

        return float(min_cost)
