"""
Problem: Next Greater Element II
LeetCode #: 503
Difficulty: Medium
Link: https://leetcode.com/problems/next-greater-element-ii/

Approach:
Since the array is circular, iterate through the array twice (length 2 * N).
Use a monotonic stack storing indices of elements.
For index `i` from `0` to `2 * N - 1`, target index is `i % N`.
While stack is non-empty and `nums[stack[-1]] < nums[i % N]`:
- Pop stack index and set `res[popped] = nums[i % N]`.
Only push index `i % N` onto stack during the first pass (`i < N`).

Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for stack and result array.
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                res[stack.pop()] = curr
            if i < n:
                stack.append(i)

        return res
