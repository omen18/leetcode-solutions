"""
Problem: Palindrome Partitioning II
LeetCode #: 132
Difficulty: Hard
Link: https://leetcode.com/problems/palindrome-partitioning-ii/

Approach: Dynamic Programming with Center Expansion. Maintain `cuts[i]` initialized to `i` (max cuts needed for prefix `s[:i+1]`).
Expand palindromes around every center (both odd and even length).
When a palindrome `s[l..r]` is found:
- If `l == 0`, `cuts[r] = 0` (no cuts needed).
- Otherwise, `cuts[r] = min(cuts[r], cuts[l-1] + 1)`.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        cuts = list(range(n))

        for i in range(n):
            # Odd length palindromes
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                cuts[r] = 0 if l == 0 else min(cuts[r], cuts[l - 1] + 1)
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                cuts[r] = 0 if l == 0 else min(cuts[r], cuts[l - 1] + 1)
                l -= 1
                r += 1

        return cuts[n - 1]
