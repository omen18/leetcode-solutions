"""
Problem: Validate Stack Sequences
LeetCode #: 946
Difficulty: Medium
Link: https://leetcode.com/problems/validate-stack-sequences/

Approach:
Simulate stack push and pop operations.
Iterate through `pushed` array, pushing each element to a stack.
After each push, while the stack top matches the current target in `popped` (index `j`),
pop from stack and increment `j`.
Return `True` if stack is empty at the end, `False` otherwise.

Time Complexity: O(N) where N is length of pushed array.
Space Complexity: O(N) for stack.
"""

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0
