"""
Problem: Jump Game VI
LeetCode #: 1696
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game-vi/

Approach: Dynamic Programming with Monotonic Deque - Maintain maximum DP value in sliding window of size k.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        # Monotonic queue storing indices with decreasing dp values
        dq = deque([0])
        
        for i in range(1, n):
            # Remove indices outside window [i - k, i - 1]
            if dq and dq[0] < i - k:
                dq.popleft()
                
            dp[i] = nums[i] + dp[dq[0]]
            
            # Maintain decreasing order in deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
                
            dq.append(i)
            
        return dp[n - 1]
