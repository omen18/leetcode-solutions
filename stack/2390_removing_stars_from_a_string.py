"""
Problem: Removing Stars From a String
LeetCode #: 2390
Difficulty: Medium
Link: https://leetcode.com/problems/removing-stars-from-a-string/

Approach:
Use a stack to build the output string.
Iterate through each character in string `s`:
- If character is '*', pop the top non-star character from stack.
- Otherwise, append character to stack.
Join stack elements to form final string.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(N) for stack.
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
