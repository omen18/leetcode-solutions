"""
Problem: Largest Divisible Subset
LeetCode #: 368
Difficulty: Medium
Link: https://leetcode.com/problems/largest-divisible-subset/

Approach: Dynamic Programming after sorting array, tracking subset length and predecessor index.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i
                
        res = []
        curr = max_idx
        while curr != -1:
            res.append(nums[curr])
            curr = parent[curr]
            
        return res[::-1]
