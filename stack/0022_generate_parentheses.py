"""
Problem: Generate Parentheses
LeetCode #: 22
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

Approach:
Use backtracking with a stack to generate all valid combinations of n pairs of parentheses.
Maintain counts of `open_count` and `close_count`.
- Add '(' if `open_count < n`.
- Add ')' if `close_count < open_count`.
Base case is reached when length of current combination equals 2 * n.

Time Complexity: O(4^n / sqrt(n)) bounded by the N-th Catalan number.
Space Complexity: O(n) recursion stack depth.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res
