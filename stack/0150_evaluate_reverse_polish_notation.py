"""
Problem: Evaluate Reverse Polish Notation
LeetCode #: 150
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach:
Use a stack to evaluate the expression. Iterate through each token in the RPN expression.
If the token is an operand, push it onto the stack. If it is an operator (+, -, *, /),
pop the top two operands from the stack (second popped is left operand, first is right operand),
apply the operation, and push the result back onto the stack. Integer division truncates towards zero.

Time Complexity: O(N) where N is the number of tokens.
Space Complexity: O(N) to store operands in the stack.
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
