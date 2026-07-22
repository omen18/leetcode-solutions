"""
Problem: Stickers to Spell Word
LeetCode #: 691
Difficulty: Hard
Link: https://leetcode.com/problems/stickers-to-spell-word/

Approach: Bitmask Dynamic Programming with Memoized BFS/DFS.
Represent the satisfied characters of `target` (length `N <= 15`) as a bitmask of length `N`.
For state `mask`, find the first unset bit `target[i]`. Only try stickers that contain `target[i]` to prune search space.
Compute new mask after using the sticker and recursively transition.
Time Complexity: O(2^N * S * N) where N = len(target) <= 15, S = len(stickers)
Space Complexity: O(2^N)
"""

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        sticker_counts = [Counter(s) for s in stickers]

        @lru_cache(None)
        def dp(mask: int) -> int:
            if mask == (1 << n) - 1:
                return 0

            # Find the first char in target that is not yet covered
            first_uncovered = -1
            for i in range(n):
                if not (mask & (1 << i)):
                    first_uncovered = i
                    break

            target_char = target[first_uncovered]
            res = float('inf')

            for count in sticker_counts:
                if count[target_char] == 0:
                    continue

                avail = Counter(count)
                next_mask = mask
                for i in range(n):
                    if not (next_mask & (1 << i)):
                        c = target[i]
                        if avail[c] > 0:
                            avail[c] -= 1
                            next_mask |= (1 << i)

                sub_res = dp(next_mask)
                if sub_res != float('inf'):
                    res = min(res, 1 + sub_res)

            return res

        ans = dp(0)
        return ans if ans != float('inf') else -1
