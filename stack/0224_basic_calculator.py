"""
Problem: Basic Calculator
LeetCode #: 224
Difficulty: Hard
Link: https://leetcode.com/problems/basic-calculator/

Approach:
Use a stack to evaluate expressions with unary/binary '+' and '-', integers, and parentheses.
Maintain `curr_res`, `sign` (1 for +, -1 for -), and `curr_num`.
Iterate character by character:
- Digit: construct multi-digit number `curr_num`.
- '+' or '-': apply previous `curr_num` with `sign` to `curr_res`, update `sign`, reset `curr_num`.
- '(': push current `(curr_res, sign)` to stack, reset `curr_res = 0` and `sign = 1`.
- ')': apply `curr_num` to `curr_res`, then pop `(prev_res, prev_sign)` from stack and update `curr_res = prev_res + prev_sign * curr_res`.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(N) for stack tracking nested parentheses levels.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res = 0
        sign = 1
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '+':
                curr_res += sign * curr_num
                sign = 1
                curr_num = 0
            elif char == '-':
                curr_res += sign * curr_num
                sign = -1
                curr_num = 0
            elif char == '(':
                stack.append((curr_res, sign))
                curr_res = 0
                sign = 1
            elif char == ')':
                curr_res += sign * curr_num
                curr_num = 0
                prev_res, prev_sign = stack.pop()
                curr_res = prev_res + prev_sign * curr_res

        return curr_res + sign * curr_num
