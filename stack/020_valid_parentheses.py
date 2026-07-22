"""
Problem: Valid Parentheses
LeetCode #: 20
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach: Use a stack to match opening/closing brackets.
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))      # True
    print(sol.isValid("()[]{}"))  # True
    print(sol.isValid("(]"))      # False
