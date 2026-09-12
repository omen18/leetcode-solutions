"""
Problem: Reverse Words in a String
LeetCode #: 151
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Approach: Split words by whitespace and join in reversed order.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))  # "blue is sky the"
