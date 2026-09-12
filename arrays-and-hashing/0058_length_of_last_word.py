"""
Problem: Length of Last Word
LeetCode #: 58
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word/

Approach: Traverse backwards from the end, skipping trailing spaces and counting characters.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))                 # 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # 4
