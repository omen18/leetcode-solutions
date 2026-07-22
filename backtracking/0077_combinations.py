"""
Problem: Combinations
LeetCode #: 77
Difficulty: Medium
Link: https://leetcode.com/problems/combinations/

Approach: Backtracking. Build combinations of length k from numbers 1 to n. Prune recursion branch early when the remaining elements are insufficient to reach length k.
Time Complexity: O(k * C(n, k))
Space Complexity: O(k) for recursion stack.
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int]) -> None:
            if len(current) == k:
                result.append(list(current))
                return
            
            need = k - len(current)
            for i in range(start, n - need + 2):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(1, [])
        return result
