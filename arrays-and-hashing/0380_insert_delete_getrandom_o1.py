"""
Problem: Insert Delete GetRandom O(1)
LeetCode #: 380
Difficulty: Medium
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

Approach: Combine list and hash map. Hash map stores element-to-index mapping. Removal swaps target with last element for O(1) pop.
Time Complexity: O(1) average for insert, remove, and getRandom.
Space Complexity: O(N) to store N elements.
"""

import random


class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.nums[-1]

        self.nums[idx] = last_val
        self.val_to_idx[last_val] = idx

        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
