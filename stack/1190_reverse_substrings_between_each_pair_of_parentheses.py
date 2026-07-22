"""
Problem: Reverse Substrings Between Each Pair of Parentheses
LeetCode #: 1190
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

Approach:
Use a stack to pair matching '(' and ')' parentheses indices (Wormhole technique).
1. First pass: find matching parenthesis pairs using a stack and build a map `pair[i] = j`.
2. Second pass: traverse string from left to right. When hitting a parenthesis '(' or ')',
   jump to its paired parenthesis index `i = pair[i]` and reverse traversal direction.
   Otherwise, append character to result.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(N) for stack and pair map.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = {}

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        direction = 1
        while i < n:
            if i in pair:
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction

        return "".join(res)
