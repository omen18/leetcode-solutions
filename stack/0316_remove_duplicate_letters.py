"""
Problem: Remove Duplicate Letters
LeetCode #: 316
Difficulty: Medium
Link: https://leetcode.com/problems/remove-duplicate-letters/

Approach:
Use a monotonic stack along with frequency counts and a set of visited characters.
- Record the remaining frequency count of each character using Counter.
- Iterate through string `s`:
  - Decrement remaining count of current char.
  - If current char is already in stack (visited), skip it.
  - While stack top is lexicographically larger than current char AND stack top char appears later in string:
    - Pop from stack and remove from visited set.
  - Push current char onto stack and add to visited set.

Time Complexity: O(N) where N is length of string s.
Space Complexity: O(1) bounded by fixed alphabet size 26.
"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        visited = set()

        for char in s:
            count[char] -= 1
            if char in visited:
                continue

            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)

            stack.append(char)
            visited.add(char)

        return "".join(stack)
