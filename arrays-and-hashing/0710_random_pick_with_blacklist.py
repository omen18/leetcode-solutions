"""
Problem: Random Pick with Blacklist
LeetCode #: 710
Difficulty: Hard
Link: https://leetcode.com/problems/random-pick-with-blacklist/

Approach: Remap blacklisted numbers in range [0, M-1] to non-blacklisted numbers in range [M, N-1] where M = N - len(blacklist).
Time Complexity: O(B log B) or O(B) for init where B is blacklist size, O(1) for pick.
Space Complexity: O(B) for hash map storing remapped values.
"""

import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.valid_count = n - len(blacklist)
        black_set = set(blacklist)

        # Numbers in [valid_count, n - 1] that are NOT blacklisted
        last = n - 1
        self.mapping = {}

        for b in blacklist:
            if b < self.valid_count:
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.valid_count - 1)
        return self.mapping.get(idx, idx)
