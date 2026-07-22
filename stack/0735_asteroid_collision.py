"""
Problem: Asteroid Collision
LeetCode #: 735
Difficulty: Medium
Link: https://leetcode.com/problems/asteroid-collision/

Approach:
Use a stack to simulate asteroid movements and collisions.
Iterate through `asteroids`:
- A collision occurs only when stack top is moving right (> 0) and current asteroid is moving left (< 0).
- While collision condition holds:
  - If top asteroid size < abs(current), top asteroid explodes (pop stack) and repeat loop.
  - If top asteroid size == abs(current), both explode (pop stack and mark current as destroyed).
  - If top asteroid size > abs(current), current asteroid explodes (mark as destroyed).
- If current asteroid was not destroyed, push it onto stack.

Time Complexity: O(N) where N is number of asteroids.
Space Complexity: O(N) for stack output.
"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                alive = False
            if alive:
                stack.append(ast)

        return stack
