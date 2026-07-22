"""
Problem: Simplify Path
LeetCode #: 71
Difficulty: Medium
Link: https://leetcode.com/problems/simplify-path/

Approach:
Split the path string by '/'. Iterate over the components:
- Ignore empty tokens and single dots '.'.
- For double dot '..', pop the last directory from stack if stack is non-empty (moving up one level).
- For valid directory names, push onto stack.
Finally join elements in stack with '/' preceded by '/'.

Time Complexity: O(N) where N is the length of path.
Space Complexity: O(N) to store path components in stack.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split("/")

        for comp in components:
            if comp == "" or comp == ".":
                continue
            elif comp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(comp)

        return "/" + "/".join(stack)
