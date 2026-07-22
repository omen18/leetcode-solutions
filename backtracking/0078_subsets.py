"""
Problem: Subsets
LeetCode #: 78
Difficulty: Medium
Link: https://leetcode.com/problems/subsets/

Approach: Backtracking. Generate all possible subsets (power set) by exploring inclusion/exclusion choices at each index start. Append current state to result at each node in decision tree.
Time Complexity: O(N * 2^N)
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int]) -> None:
            result.append(list(current))
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return result
