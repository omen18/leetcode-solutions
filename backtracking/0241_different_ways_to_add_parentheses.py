"""
Problem: Different Ways to Add Parentheses
LeetCode #: 241
Difficulty: Medium
Link: https://leetcode.com/problems/different-ways-to-add-parentheses/

Approach: Divide and Conquer / Backtracking with memoization. Split expression at each operator ('+', '-', '*'), recursively compute left and right sub-results, and combine them.
Time Complexity: O(4^N / sqrt(N)) Catalan number scaling.
Space Complexity: O(4^N / sqrt(N)) space for memoization and results.
"""

from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]
            
            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
                                
            if not res:
                res.append(int(expr))
                
            memo[expr] = res
            return res
        
        return compute(expression)
