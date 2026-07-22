"""
Problem: Min Stack
LeetCode #: 155
Difficulty: Medium
Link: https://leetcode.com/problems/min-stack/

Approach:
Maintain a main stack paired with the minimum element at that stack level.
Each element pushed onto the stack is stored as a tuple `(val, current_min)` where
`current_min` is `min(val, current_min_so_far)`. This allows O(1) retrieval of the minimum element.

Time Complexity: O(1) for push, pop, top, and getMin operations.
Space Complexity: O(N) where N is the number of elements in the stack.
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
