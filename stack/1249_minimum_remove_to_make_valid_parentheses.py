"""
Problem: Minimum Remove to Make Valid Parentheses
LeetCode #: 1249
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Approach:
Use a stack to keep track of indices of unmatched opening parentheses '('.
Convert input string to a list of characters for mutable operations.
- Iterate through string:
  - If '(' is encountered, push its index to stack.
  - If ')' is encountered:
    - If stack is non-empty, pop matching '(' index.
    - If stack is empty, mark current ')' for removal by replacing it with empty string.
- Any leftover indices in stack represent unmatched '(' parentheses; replace them with empty string.
Join and return list of characters.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(N) for stack and mutable character list.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []

        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ""

        while stack:
            s_list[stack.pop()] = ""

        return "".join(s_list)
