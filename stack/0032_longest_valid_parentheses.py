"""
Problem: Longest Valid Parentheses
LeetCode #: 32
Difficulty: Hard
Link: https://leetcode.com/problems/longest-valid-parentheses/

Approach:
Use a stack to keep track of indices of parentheses.
Initialize stack with -1 as a base boundary for valid substring calculations.
Iterate through string `s`:
- If char is '(', push index `i` onto stack.
- If char is ')':
  - Pop top of stack.
  - If stack becomes empty, push current index `i` as new boundary.
  - If stack is non-empty, current valid length is `i - stack[-1]`; update max_len.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(N) for stack.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
