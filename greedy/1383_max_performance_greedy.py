"""
Problem: Maximum Performance of a Team
LeetCode #: 1383
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-performance-of-a-team/

Approach: Sort engineers by efficiency descending. Use min-heap of speed to maintain top k speeds for current minimum efficiency.
Time Complexity: O(N log N + N log K)
Space Complexity: O(N + K)
"""

import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)
        
        speed_heap = []
        speed_sum = 0
        max_perf = 0
        MOD = 10**9 + 7
        
        for eff, sp in engineers:
            heapq.heappush(speed_heap, sp)
            speed_sum += sp
            
            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)
                
            max_perf = max(max_perf, speed_sum * eff)
            
        return max_perf % MOD
