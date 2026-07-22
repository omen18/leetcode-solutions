"""
Problem: Combination Sum
LeetCode #: 39
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum/

Approach: Backtracking. Explore combinations starting from index 'start'. Since elements can be reused, pass 'start' index as 'i' in recursive calls. Prune search when remaining target < 0.
Time Complexity: O(2^T) where T is target / min(candidates).
Space Complexity: O(T) for recursion stack.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int], remain: int) -> None:
            if remain == 0:
                result.append(list(current))
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remain - candidates[i])
                current.pop()
                
        backtrack(0, [], target)
        return result
