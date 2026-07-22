"""
Problem: Subsets II
LeetCode #: 90
Difficulty: Medium
Link: https://leetcode.com/problems/subsets-ii/

Approach: Backtracking on sorted array. Avoid duplicate subsets by skipping duplicate elements at the same recursion level (if i > start and nums[i] == nums[i - 1]).
Time Complexity: O(N * 2^N)
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(start: int, current: List[int]) -> None:
            result.append(list(current))
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return result
