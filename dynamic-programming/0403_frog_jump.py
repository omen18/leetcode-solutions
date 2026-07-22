"""
Problem: Frog Jump
LeetCode #: 403
Difficulty: Hard
Link: https://leetcode.com/problems/frog-jump/

Approach: Dynamic Programming with Hash Map.
Map each stone to a set of possible jump sizes that can reach it.
For stone position `pos` and jump size `k`, attempt jumps of size `k - 1`, `k`, and `k + 1`.
If `next_pos = pos + next_k` is a valid stone, add `next_k` to `dp[next_pos]`.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[1].add(1)

        last_stone = stones[-1]

        for stone in stones:
            for k in dp[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0:
                        next_stone = stone + step
                        if next_stone == last_stone:
                            return True
                        if next_stone in stone_set:
                            dp[next_stone].add(step)

        return len(dp[last_stone]) > 0
