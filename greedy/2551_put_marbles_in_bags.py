"""
Problem: Put Marbles in Bags
LeetCode #: 2551
Difficulty: Hard
Link: https://leetcode.com/problems/put-marbles-in-bags/

Approach: Partition boundaries add weights[i] + weights[i+1] to total score. Compute all adjacent pair sums, sort them, and return difference between top (k-1) and bottom (k-1) pair sums.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
            
        pair_weights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair_weights.sort()
        
        min_sum = sum(pair_weights[:k - 1])
        max_sum = sum(pair_weights[len(pair_weights) - (k - 1):])
        
        return max_sum - min_sum
