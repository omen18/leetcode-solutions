"""
Problem: Combination Sum III
LeetCode #: 216
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iii/

Approach: Backtracking. Pick k distinct numbers from 1 to 9 that sum to n. Recursively choose elements, pruning when current length reaches k or remaining target sum < 0.
Time Complexity: O(C(9, k))
Space Complexity: O(k) for recursion stack.
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int], remain: int) -> None:
            if len(current) == k:
                if remain == 0:
                    result.append(list(current))
                return
            if remain < 0:
                return
            
            for i in range(start, 10):
                if i > remain:
                    break
                current.append(i)
                backtrack(i + 1, current, remain - i)
                current.pop()
                
        backtrack(1, [], n)
        return result
