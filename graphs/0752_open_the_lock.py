"""
Problem: Open the Lock
LeetCode #: 752
Difficulty: Medium
Link: https://leetcode.com/problems/open-the-lock/

Approach: BFS on 4-digit lock states. Each wheel can be rotated forward (+1) or backward (-1).
Treat deadends as blocked states. Execute level-by-level BFS from "0000" to reach target.

Time Complexity: O(N * 10^D) where D=4 digits, resulting in at most 10,000 states.
Space Complexity: O(10^D) for queue and visited set.
"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            curr, steps = queue.popleft()

            for i in range(4):
                digit = int(curr[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    nxt = curr[:i] + str(new_digit) + curr[i + 1 :]

                    if nxt == target:
                        return steps + 1

                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))

        return -1
