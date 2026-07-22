"""
Problem: Freedom Trail
LeetCode #: 514
Difficulty: Hard
Link: https://leetcode.com/problems/freedom-trail/

Approach: Dynamic Programming with Hash Map. Map each character in `ring` to its list of indices.
`dp[pos]` stores the minimum steps to spell the key up to current character ending with ring index `pos`.
For each character in `key`, transition from all valid previous ring positions `p` to current valid positions `c`.
Distance between indices `p` and `c` on ring of size `R` is `min(abs(p - c), R - abs(p - c))`.
Time Complexity: O(K * R^2) where K = len(key), R = len(ring)
Space Complexity: O(R)
"""

from collections import defaultdict
from typing import List


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        r_len = len(ring)
        pos_map = defaultdict(list)
        for i, ch in enumerate(ring):
            pos_map[ch].append(i)

        # dp maps ring index to min steps
        dp = {0: 0}

        for char in key:
            next_dp = {}
            for next_pos in pos_map[char]:
                min_steps = float('inf')
                for curr_pos, steps in dp.items():
                    diff = abs(curr_pos - next_pos)
                    dist = min(diff, r_len - diff)
                    min_steps = min(min_steps, steps + dist + 1)
                next_dp[next_pos] = min_steps
            dp = next_dp

        return min(dp.values())
