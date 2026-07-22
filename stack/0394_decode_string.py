"""
Problem: Decode String
LeetCode #: 394
Difficulty: Medium
Link: https://leetcode.com/problems/decode-string/

Approach:
Use a stack to store previous string segments and repeat counts.
Iterate through the string s:
- If character is a digit, update current count `k = k * 10 + int(char)`.
- If character is '[', push current string and `k` to stack, then reset current string and `k`.
- If character is ']', pop `(prev_str, count)` from stack and update current string to `prev_str + curr_str * count`.
- If character is a letter, append it to current string.

Time Complexity: O(M) where M is length of decoded string.
Space Complexity: O(M) for stack and result strings.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                stack.append((curr_str, k))
                curr_str = ""
                k = 0
            elif char == "]":
                prev_str, count = stack.pop()
                curr_str = prev_str + curr_str * count
            else:
                curr_str += char

        return curr_str
