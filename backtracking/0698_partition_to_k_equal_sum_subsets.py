"""
Problem: Partition to K Equal Sum Subsets
LeetCode #: 698
Difficulty: Medium
Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Approach: Backtracking with Bitmasking and Memoization. Target sum per subset is sum(nums) / k. Maintain a bitmask of used numbers and current subset sum.
Time Complexity: O(N * 2^N)
Space Complexity: O(2^N) for memoization dictionary.
"""

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        
        memo = {}
        n = len(nums)
        
        def backtrack(mask: int, current_sum: int) -> bool:
            if mask == (1 << n) - 1:
                return True
            if (mask, current_sum) in memo:
                return memo[(mask, current_sum)]
            
            for i in range(n):
                if not (mask & (1 << i)):
                    if current_sum + nums[i] > target:
                        continue
                    next_sum = 0 if current_sum + nums[i] == target else current_sum + nums[i]
                    if backtrack(mask | (1 << i), next_sum):
                        memo[(mask, current_sum)] = True
                        return True
                    
            memo[(mask, current_sum)] = False
            return False
        
        return backtrack(0, 0)
