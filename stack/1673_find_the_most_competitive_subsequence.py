"""
Problem: Find the Most Competitive Subsequence
LeetCode #: 1673
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-most-competitive-subsequence/

Approach:
Use a monotonic stack to construct the lexicographically smallest subsequence of length k.
Iterate through `nums`. For each element:
- Pop from stack while stack is non-empty, stack top > element, and remaining elements in `nums`
  plus current stack length is greater than `k` (ensuring we can still form a subsequence of length k).
- If stack length < k, append element to stack.

Time Complexity: O(N) where N is length of nums.
Space Complexity: O(k) for stack.
"""

from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)

        return stack
