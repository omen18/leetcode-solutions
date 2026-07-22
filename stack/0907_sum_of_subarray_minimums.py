"""
Problem: Sum of Subarray Minimums
LeetCode #: 907
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-subarray-minimums/

Approach:
For each element `arr[i]`, find how many subarrays have `arr[i]` as their minimum value.
Use a monotonic stack to determine:
- Distance to Previous Strictly Less Element (left distance `mid - left_bound`).
- Distance to Next Less or Equal Element (right distance `right_bound - mid`).
The number of subarrays where `arr[mid]` is the minimum is `left_dist * right_dist`.
Sum `arr[mid] * left_dist * right_dist` for all elements modulo 10^9 + 7.

Time Complexity: O(N) where N is length of arr.
Space Complexity: O(N) for monotonic stack.
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        res = 0

        # Append dummy element at index n to flush remaining stack elements
        for i in range(n + 1):
            curr_val = arr[i] if i < n else float('-inf')
            while stack and arr[stack[-1]] > curr_val:
                mid = stack.pop()
                left_bound = stack[-1] if stack else -1
                right_bound = i
                count = (mid - left_bound) * (right_bound - mid)
                res = (res + arr[mid] * count) % MOD
            stack.append(i)

        return res
