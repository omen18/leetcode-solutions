"""
Problem: Paint Fence
LeetCode #: 276
Difficulty: Medium
Link: https://leetcode.com/problems/paint-fence/

Approach: Dynamic Programming - Maintain count of valid colorings where current post matches previous (same) or differs (diff).
Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
            
        same = k
        diff = k * (k - 1)
        
        for _ in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)
            
        return same + diff
