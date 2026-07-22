"""
Problem: Random Pick Index
LeetCode #: 398
Difficulty: Medium
Link: https://leetcode.com/problems/random-pick-index/

Approach: Build hash map mapping each target value to list of indices. Randomly select an index from list on pick.
Time Complexity: O(N) for init, O(1) for pick.
Space Complexity: O(N) to store index lists.
"""

from collections import defaultdict
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])
