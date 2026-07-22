"""
Problem: Remove K Digits
LeetCode #: 402
Difficulty: Medium
Link: https://leetcode.com/problems/remove-k-digits/

Approach:
To construct the smallest possible number, use a greedy strategy with a monotonic increasing stack.
Iterate through digits of `num`:
- While `k > 0`, stack is non-empty, and top of stack > current digit, pop from stack and decrement `k`.
- Push current digit onto stack.
If `k > 0` after loop, pop remaining `k` elements from end of stack.
Strip leading zeros from result. Return "0" if result string is empty.

Time Complexity: O(N) where N is length of num string.
Space Complexity: O(N) for stack.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0, remove remaining k digits from end
        if k > 0:
            stack = stack[:-k]

        # Strip leading zeros
        res = "".join(stack).lstrip("0")
        return res if res else "0"
