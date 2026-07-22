"""
Problem: Basic Calculator II
LeetCode #: 227
Difficulty: Medium
Link: https://leetcode.com/problems/basic-calculator-ii/

Approach: Single pass using stack to evaluate multiplication/division immediately and sum addition/subtraction.
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        operator = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    stack.append(stack.pop() * curr_num)
                elif operator == "/":
                    # Truncate toward zero integer division
                    prev = stack.pop()
                    stack.append(int(prev / curr_num))

                operator = char
                curr_num = 0

        return sum(stack)
