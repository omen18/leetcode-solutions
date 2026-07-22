"""
Problem: Snapshot Array
LeetCode #: 1146
Difficulty: Medium
Link: https://leetcode.com/problems/snapshot-array/

Approach: Maintain history per element as a list of `(snap_id, value)`. `set` appends or updates entry for current snap_id. `get` uses binary search (bisect_right) to find value at largest snap_id <= target snap_id.
Time Complexity: set: O(1), snap: O(1), get: O(log S) where S is number of snaps for element
Space Complexity: O(N + total set operations)
"""

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = (
            bisect.bisect_right(
                self.history[index], (snap_id, float("inf"))
            )
            - 1
        )
        return self.history[index][idx][1]
