"""
Problem: Sum of Total Strength of Wizards
LeetCode #: 2281
Difficulty: Hard
Link: https://leetcode.com/problems/sum-of-total-strength-of-wizards/

Approach:
For each wizard `strength[i]`, find the range `[L+1, R-1]` where `strength[i]` is the minimum.
To handle duplicate values without overcounting:
- Left bound `L`: index of Previous Strictly Less element.
- Right bound `R`: index of Next Less or Equal element.

The total strength of all subarrays where `strength[i]` is minimum is `strength[i] * sum(sum(subarray))`.
Using prefix sums `pref` and prefix sums of prefix sums `pref_pref`:
`sum_{l=L+1}^i sum_{r=i}^{R-1} sum(strength[l...r]) = (i - L) * (pref_pref[R+1] - pref_pref[i+1]) - (R - i) * (pref_pref[i+1] - pref_pref[L+1])`.

Time Complexity: O(N) where N is length of strength array.
Space Complexity: O(N) for prefix sums and monotonic stacks.
"""

from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] + strength[i]) % MOD

        pref_pref = [0] * (n + 2)
        for i in range(n + 1):
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % MOD

        res = 0
        for i in range(n):
            L, R = left[i], right[i]
            left_part = (i - L) * (pref_pref[R + 1] - pref_pref[i + 1])
            right_part = (R - i) * (pref_pref[i + 1] - pref_pref[L + 1])
            total_sum = (left_part - right_part) % MOD
            res = (res + strength[i] * total_sum) % MOD

        return res
