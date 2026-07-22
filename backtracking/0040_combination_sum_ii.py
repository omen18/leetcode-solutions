"""
Problem: Combination Sum II
LeetCode #: 40
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-ii/

Approach: Backtracking on sorted candidates. Each candidate can be used at most once. Avoid duplicate combinations by skipping identical elements at the same tree depth.
Time Complexity: O(2^N)
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start: int, current: List[int], remain: int) -> None:
            if remain == 0:
                result.append(list(current))
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                current.append(candidates[i])
                backtrack(i + 1, current, remain - candidates[i])
                current.pop()
                
        backtrack(0, [], target)
        return result
